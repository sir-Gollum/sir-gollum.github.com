#!/usr/bin/env python3
"""Smoke-test a running instance of the blog.

Usage:
    python check_site.py                  # defaults to http://localhost:1313
    python check_site.py https://mukomolov.com
"""

import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin

import requests

DEFAULT_BASE = "http://localhost:1313"

# Pages that must exist and return 200.
REQUIRED_PATHS = [
    # EN
    "/",
    "/blog/",
    "/tags/",
    # RU
    "/ru/",
    "/ru/blog/",
    "/ru/tags/",
    # RSS feeds
    "/index.xml",
    "/blog/index.xml",
    "/ru/index.xml",
    "/ru/blog/index.xml",
    # Static / legal pages
    "/impressum/",
    "/datenschutz/",
]


def url(base: str, path: str) -> str:
    return urljoin(base.rstrip("/") + "/", path.lstrip("/"))


def check_status(session: requests.Session, base: str, path: str) -> bool:
    u = url(base, path)
    try:
        r = session.get(u, timeout=10)
    except requests.RequestException as e:
        print(f"  FAIL {path} — {e}")
        return False
    if r.status_code != 200:
        print(f"  FAIL {path} — HTTP {r.status_code}")
        return False
    if len(r.content) == 0:
        print(f"  FAIL {path} — empty body")
        return False
    print(f"  OK   {path}")
    return True


def check_html_has_links(session: requests.Session, base: str, path: str, expected_substrings: list[str]) -> bool:
    """Check that an HTML page contains certain link substrings."""
    u = url(base, path)
    r = session.get(u, timeout=10)
    body = r.text
    ok = True
    for s in expected_substrings:
        if s not in body:
            print(f"  FAIL {path} — missing expected link/text: {s!r}")
            ok = False
    return ok


def check_rss(session: requests.Session, base: str, path: str) -> bool:
    """Validate RSS feed: must be valid XML with at least one <item>."""
    u = url(base, path)
    try:
        r = session.get(u, timeout=10)
    except requests.RequestException as e:
        print(f"  FAIL {path} RSS — {e}")
        return False

    try:
        root = ET.fromstring(r.content)
    except ET.ParseError as e:
        print(f"  FAIL {path} RSS — invalid XML: {e}")
        return False

    # RSS items live under channel/item (with possible namespace)
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    items = root.findall(f".//{ns}item")
    if not items:
        print(f"  FAIL {path} RSS — no <item> elements found")
        return False

    # Every item must have a title and link
    ok = True
    for item in items:
        title = item.find(f"{ns}title")
        link = item.find(f"{ns}link")
        if title is None or not (title.text or "").strip():
            print(f"  FAIL {path} RSS — item missing <title>")
            ok = False
        if link is None or not (link.text or "").strip():
            print(f"  FAIL {path} RSS — item missing <link>")
            ok = False

    if ok:
        print(f"  OK   {path} RSS — {len(items)} items")
    return ok


def discover_post_links(session: requests.Session, base: str, blog_path: str) -> list[str]:
    """Extract post links from the blog listing page."""
    u = url(base, blog_path)
    r = session.get(u, timeout=10)
    body = r.text

    # Simple extraction: find href values that look like blog post links.
    import re
    links = re.findall(r'href="(/(?:ru/)?blog/\d{4}/\d{2}/[^"]+)"', body)
    return sorted(set(links))


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BASE
    print(f"Checking site at {base}\n")

    session = requests.Session()
    # Use a browser-like UA to avoid being blocked
    session.headers["User-Agent"] = "blog-check/1.0"

    ok = True

    # 1. Required pages return 200
    print("--- Required pages ---")
    for path in REQUIRED_PATHS:
        if not check_status(session, base, path):
            ok = False

    # 2. Navigation links present on key pages
    print("\n--- Navigation (EN) ---")
    if not check_html_has_links(session, base, "/", ["/blog/", "/tags/"]):
        ok = False
    else:
        print("  OK   / has blog & tags links")

    print("\n--- Navigation (RU) ---")
    if not check_html_has_links(session, base, "/ru/", ["/ru/blog/", "/ru/tags/"]):
        ok = False
    else:
        print("  OK   /ru/ has blog & tags links")

    # 3. Discover and check individual blog posts
    print("\n--- Blog posts (EN) ---")
    en_posts = discover_post_links(session, base, "/blog/")
    if not en_posts:
        print("  FAIL no blog post links found on /blog/")
        ok = False
    else:
        for p in en_posts:
            if not check_status(session, base, p):
                ok = False

    print("\n--- Blog posts (RU) ---")
    ru_posts = discover_post_links(session, base, "/ru/blog/")
    if not ru_posts:
        print("  FAIL no blog post links found on /ru/blog/")
        ok = False
    else:
        for p in ru_posts:
            if not check_status(session, base, p):
                ok = False

    # 4. RSS feeds
    print("\n--- RSS feeds ---")
    for feed in ["/index.xml", "/blog/index.xml", "/ru/index.xml", "/ru/blog/index.xml"]:
        if not check_rss(session, base, feed):
            ok = False

    # 5. RSS items point to reachable pages
    print("\n--- RSS link reachability ---")
    for feed in ["/index.xml", "/ru/index.xml"]:
        u = url(base, feed)
        r = session.get(u, timeout=10)
        root = ET.fromstring(r.content)
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"
        for item in root.findall(f".//{ns}item"):
            link_el = item.find(f"{ns}link")
            if link_el is not None and link_el.text:
                link_url = link_el.text.strip()
                try:
                    resp = session.get(link_url, timeout=10)
                    if resp.status_code != 200:
                        print(f"  FAIL RSS link {link_url} — HTTP {resp.status_code}")
                        ok = False
                    else:
                        print(f"  OK   {link_url}")
                except requests.RequestException as e:
                    print(f"  FAIL RSS link {link_url} — {e}")
                    ok = False

    # Summary
    print()
    if ok:
        print("All checks passed.")
        return 0
    else:
        print("Some checks FAILED.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
