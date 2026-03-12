+++
date = '2012-07-10T20:20:05+02:00'
draft = false
title = 'Moscow Django Meetup'
tags = ["Django", "Python"]
type = "posts"
+++

Until recently, I really envied Ukrainians because they have a pretty solid Python community. There are tons of conferences — off the top of my head, I remember [Kiyv.py][1], [KharkivPy][2], [PyConUA][3], and I'm sure the Python scene was buzzing at less formal meetups too. In Moscow, nothing like that existed, even though quite a few Python developers attended [Yandex.Saturday][4], [YaC][5], [DevConf][6], and other events. As it turns out, I wasn’t the only one who felt that way.

In February–March, some developers from the [FutureColors][7] web studio got together, made a [Facebook group][8], and invited everyone interested to the first informal meetup for Django developers. At the time, I was pretty far from Moscow, so I only found out about it after they posted a report on Habrahabr. Since then, there have been three more meetups, I’ve been to two of them. Now the venue seems to have settled in, and recently they even launched a [website][8] for the meetup.

At yesterday’s fourth meetup, there were three talks:

* [Handling HTTP Requests in Python][9]. The talk was about how to separate application business logic from the protocol being used. Basically, instead of passing a request parameter and pulling the needed data out of it in the handler, you define a transformation so that the data arrives in the right format from the start. There's a library implementation [on GitHub][10] — I’ll have to check it out when I get the chance.
* [Django and Continuous Integration][10]. This one covered how to use [Jenkins][11] to build and test Django projects, with a bit of mention of [Travis][12], which is gaining popularity in open-source projects. Since the last time I set up Jenkins for Django, things have gotten much simpler: there’s now [django-jenkins][13] and a [handy plugin][14] for Jenkins to work with Python projects. I used to do it all manually with shell scripts — definitely time for an upgrade.
* Setting up a Django project from scratch using the PyCharm IDE. The speaker promised to make a screencast — I’ll add a link here when it's up. Learned a couple of new things, like how to integrate pep8 checking into PyCharm.

Also at yesterday’s meetup, people were more actively discussing the possibility of the community participating in Django Dash, which will probably happen on August 17–19. Sounds like it’s worth a shot.

[1]: http://kyivpy.org.ua/
[2]: http://kharkivpy.org.ua/
[3]: http://ua.pycon.org/
[4]: http://events.yandex.ru/events/yasubbotnik/
[5]: http://events.yandex.ru/events/yac/
[6]: http://www.devconf.ru/
[7]: http://futurecolors.ru/
[8]: http://www.facebook.com/groups/367203686641943/
[9]: http://braintrace.ru/talks/abstracting-http.ru.html#1
[10]: https://speakerdeck.com/u/moscowdjango/p/django-continuous-integration
[11]: http://jenkins-ci.org/
[12]: http://travis-ci.org/
[13]: https://github.com/kmmbvnr/django-jenkins
[14]: https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin
