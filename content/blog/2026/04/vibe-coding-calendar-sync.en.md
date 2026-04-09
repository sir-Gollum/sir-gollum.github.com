+++
date = '2026-04-09T20:30:00+02:00'
draft = false
title = 'Vibe-coding a Calendar Sync Tool'
tags = ['tools', 'ai', 'swift']
type = "posts"
+++

I wanted to get a post out before I leave for a relatively long trip. This is the first post after relaunching the blog, and it would be funny if I promised myself to write more often and then disappeared again for who knows how long. I've done that before - about 13 years ago, and I wouldn't want to repeat the pattern now.

<!--more-->

### The Vibe Coding Dopamine Loop

Normally, I try to squeeze in an hour or two of gaming on most workdays, plus sometimes on weekends. Last summer however, that time went to coding instead - or more precisely, to "vibe coding", or even more precisely, to AI-assisted coding (since I actually looked at the generated code and made changes to it). There is a certain dopamine loop to the process of making "one more prompt" that's very familiar from video games ([Heroes 3](https://en.wikipedia.org/wiki/Heroes_of_Might_and_Magic_III), anyone?).

I experimented with a few AI-assisted coding tools - [Zed Editor](https://zed.dev/), [GitHub Copilot](https://github.com/features/copilot) - and ended up building a [small project](https://github.com/sir-Gollum/CalSync1on1) and open-sourcing it. The project is likely not interesting to anyone other than myself, but it's what led me to relaunch this blog - I wanted to write about it as a wrap on the project.

### The Problem

For more than a decade, my wife and I have a shared calendar - it's convenient for planning activities together like trips or concerts. Among other things, I use this shared calendar to signal when I have one-on-one meetings at work and need some quiet time. We live in a small apartment, so having a visible block of time when I shouldn't be disturbed is convenient.

For a while, I handled this manually by adding events to the shared calendar. The problem is that my one-on-ones move around a lot - they get rescheduled, shifted, or cancelled. Updating them manually is tedious, so I decided to write a small automation for this chore.

### The Solution - CalSync1on1

The result is [CalSync1on1](https://github.com/sir-Gollum/CalSync1on1) - a small CLI utility written in Swift for macOS that uses Apple's [EventKit](https://developer.apple.com/documentation/eventkit) framework to work with system calendars. One constraint I had was that I needed to keep my work calendar private - I can't (and shouldn't) share it directly.

The tool looks at both my work and personal calendars on macOS - the personal one being the calendar shared with my wife. It scans events over a configurable time window (the current and the next week by default) and synchronizes the ones it recognizes as one-on-ones. The detection is straightforward: if a meeting has exactly two attendees including me, it's a one-on-one. It is a bit more complex with recurring meetings due to their different internal organization, but those are also covered by my implementation.

There are a few filters on top of that - the tool skips all-day events, events with certain substrings in the title, and private events. Synced events get a clean and configurable title like `1:1 with [Name]` so nothing sensitive leaks from my work calendar.

One thing I'm pretty happy with is how the sync tracking works: instead of a database or any other external state, the tool embeds metadata directly into the destination calendar events. This metadata is then used to track which events need to be modified. When meetings get rescheduled or cancelled, the shared calendar reflects that automatically. It's a small thing, but it removes a constant source of friction.

The tool runs on a schedule via macOS [launchd](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac) and syncs calendars every 30 minutes, so I don't have to think about it - everything happens on its own.

### On AI-Assisted Coding

I built the project in about a week, including basic build automation and [GitHub Actions](https://github.com/sir-Gollum/CalSync1on1/actions) for releases. The code isn't perfect, but it's functional - I reviewed it and added a set of tests that cover the functionality pretty well. I wrote very little of the code manually - mostly generated it with Copilot over several iterations, then refactored and restructured.

The tool works and does what it should, so I haven't felt much need to update it since. Looking back, it's exciting how much AI coding tools have evolved even in the last 6 to 9 months since I built it. With modern tools, almost anyone can build increasingly complex and useful things to simplify their own work or life. Kind of like how [Twitter Bootstrap](/blog/2012/06/twitter-bootstrap/) once made it possible for hard-core back-end developers to build decent-looking websites - AI coding tools are now doing a similar thing for the gap between "I have an idea" and "I have a working service" :)

I might write more about this - I work with GenAI a lot at my day job, so there's plenty to say about building and using AI tools and agents to automate work and day-to-day tasks.

But for now - first post after the relaunch is done :)
