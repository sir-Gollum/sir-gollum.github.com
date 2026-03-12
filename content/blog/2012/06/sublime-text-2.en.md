+++
date = '2012-06-02T15:18:21+02:00'
draft = false
title = 'Sublime Text 2'
tags = ['tools', 'python']
type = "posts"
+++

I was just finishing up [Jeff Atwood's article](https://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/) and was about to sit down to watch lectures on [HCI](http://www.coursera.org/course/hci) when the lights flickered and the internet went out. I was planning to write here today anyway, but I wanted to do it closer to evening.

Today let's talk about work tools. As it happens, a programmer's main tool is a text editor. Sure, there are IDEs of varying degrees of sophistication that provide lots of different functionality, can work with plugins, and allow you to change the environment beyond recognition through extensions. But the most powerful IDEs still remain, at their core, text editors wrapped with additional functionality.

For editing text and relatively simple scripts, I typically use a lightweight editor, and save the full-featured development environment for something more substantial. The development environment depends on the language I'm writing in at the moment, but I've used various lightweight editors on different systems — on Windows it was [Notepad++](http://notepad-plus-plus.org/) for a long time, on Mac it was [Smultron](http://www.peterborgapps.com/smultron/).

Some time ago, from the well-known-in-certain-circles [Radio-T podcast](http://radio-t.com), I learned about the new version of the [Sublime Text 2](http://www.sublimetext.com/2) editor. The podcast hosts spoke about it so enthusiastically that I couldn't resist and went to try it out. The editor really impressed me, and although it's currently in beta status, it has almost completely replaced the editors I used before.

The main advantage of Sublime Text 2 is its simple and convenient plugin system and overall flexibility of configuration. Plugins are written in Python, which I've been happily using for about four years now, and the API for developing plugins is quite straightforward. You can add almost anything to the editor with plugins — for example, for a contest from the same Radio-T and as part of getting familiar with the plugin system, I wrote [two plugins](http://bitbucket.org/sir_gollum/sublimeplugins):

* One does Code Folding by region/endregion tags
* The other typographically formats text in the current buffer using a [typography service](http://typograf.ru).

Another plugin I use frequently is [SublimeREPL](http://bitbucket.org/wuub/sublimerepl/wiki/Home), which embeds consoles for a bunch of things into the editor (Python, Ruby, various shells).

Plugins, themes, and other extensions are very easy to add and configure. It's easy to plug in an existing library — for example, there are several [attempts](http://bitbucket.org/theblacklion/sublime_orgmode/) to [port](http://github.com/danielmagnussons/orgmode) org-mode from EMACS.

Plugins are actively being written, and there's even a package manager for installing them, which can be added with this one-liner:

```python
import urllib2,os
pf='Package Control.sublime-package'
ipp=sublime.installed_packages_path()
os.makedirs(ipp) if not os.path.exists(ipp) else None
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()))
open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())
print 'Please restart Sublime Text to finish installation'
```

To add the package manager, you need to execute this code in the editor's console, which is called up with ctrl+`. After execution, the command "Package Control: Install Package" is added to the command list, which is called up with cmd+shift+p by default.

Additionally, the editor is cross-platform and works on any system I use.

Another nice feature is the recently trendy Distraction-Free Mode, which removes everything from the screen except the text. I use this mode when writing blog posts :)

And of course, a ton of standard text editor features for programmers — macros, syntax highlighting, project management and so on — are available in Sublime Text 2 out of the box.

Now about the features I'm still missing.

* First — the ability to set a default encoding for new files. There's a menu item "Open with Encoding...", and if you use it, the editor will save the file in the same encoding it opened with, but to create files directly in the needed encoding instead of Unicode — it seems you need to write a plugin for that. On Unix systems this doesn't cause any inconvenience, but at work FAR Manager users asked to use cp1251.
* Second — the ability to prompt for a password on Mac when there aren't enough privileges to modify a file. It can't do this yet, and even if you run it with sudo, it won't save the file.

And one more potential downside that's also a plus — the editor is graphical. Everything looks quite nice, but if you only have a console — use good old vi, which is available everywhere :)

In short, if you haven't tried it yet — I highly recommend it. The editor is paid, but the trial is unlimited. As I understand it, the author's approach is that people who enjoy using a quality product will pay anyway. In my opinion, that's the right approach.

And as a follow-up, a recent article on [how to set up Sublime Text 2 for web and Python development](http://opensourcehacker.com/2012/05/11/sublime-text-2-tips-for-python-and-web-developers/).
