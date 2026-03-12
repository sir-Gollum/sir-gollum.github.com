+++
date = '2012-06-18T20:37:48+02:00'
draft = false
title = 'Twitter Bootstrap'
tags = ['tools', 'web']
type = "posts"
+++

[@Yuki_Sumaguro](http://twitter.com/Yuki_Sumaguro) and I are working on a non-commercial project to create a small website. Generally speaking, my markup / layout skills are in a rather rudimentary state, since I haven't had to do much layout work. And when I did, I produced something rather mockup-like.

But now the task is to make a website, preferably from scratch. Accordingly, I'll have to come up with a design, do the layout, whip up something in JS, and code the server part, albeit a simple one.

At one point [@hellodrw](http://twitter.com/hellodrw) advised me to learn layout starting with HTML4, then moving on to xHTML and so on. But that takes a long time, and I want to launch the site sooner rather than later. Besides, I've never had any particular desire to become a layout specialist: for me, most of a layout person's work comes down to finding and attempting to fix rendering bugs in different browsers, and the number of bugs and incompatibilities keeps growing. In short, not the most inspiring work :)

At first I was looking at [SASS](http://sass-lang.com/) and writing CSS from scratch, but it's not really suitable for my case, because when you lack knowledge, it's easier to take some ready-made solutions and figure them out, modifying and adding to them as you go.
This is exactly the approach that [Twitter's Bootstrap](http://twitter.github.com/bootstrap/) allows you to use successfully.

Bootstrap is essentially a very simple yet quite powerful thing. It's a set of CSS files and a small instruction manual that allows you to quite easily lay out a typical grid used in most websites today. It's well suited for a blog, news site, or some other content-oriented website. But it can quite well serve as a starting point for something more complex too.

### Grid

Bootstrap is based on a standard 960-pixel-wide grid. The grid is divided into blocks of different widths, which can be combined in a relatively arbitrary way, forming columns and sections. Columns can be nested within each other, creating the desired layout. Bootstrap development uses `less`, and if you take the `less` source files, you can easily customize things like the maximum number of columns (16 by default), site width, color scheme and so on - the resulting sizes and colors will adjust when generating the final CSS.

### Ready-made Layouts

The documentation describes examples of using Bootstrap to get typical CSS layouts. If the site you need to make fits one of them by 70-80% - you can just take it and use it with minor modifications.

### Typography

This includes prepared styles for headings, paragraphs, lists, source code and so on. These styles are also adjustable via `less`, but you can quite easily tweak something in CSS as well.

### Labels

Colored badges with trendy rounded corners and arbitrary text. They're made very easily and naturally.

### Galleries

A simple and convenient grid for laying out a grid with photo and video previews. It's defined as a list, adjusts to content size. The documentation, by the way, demonstrates all this using the example of the rather convenient layout microservice [placehold.it](http://placehold.it), which can be used to generate placeholder images of the required size.

### Tables

If you need to present information in a tabular form, Bootstrap will make your live easier here too. There are also several ready-made table style options: "dense", "sparse", with even row coloring and without it. It's very easy to implement local table sorting in JS - there's a ready-made script provided for this.

### Forms and Buttons

Here you get visually consistent styles for input fields, with added styles for displaying typical states - successful and erroneous input, field unavailability (read-only), and so on. Fields, judging by the examples, can be easily combined - for example, you can make a visually unified component from a checkbox and an input field. Buttons with gradients and rounded corners are easily made in arbitrary sizes, button colors are consistent with style names (success, warning, and so on).

### Navigation

You can use a link panel permanently hanging at the top, as done in the documentation itself. There are also styles for implementing tabs, pill buttons, breadcrumbs and pagination.

### Notifications

Bootstrap implements a large number of different nice pop-up notifications, tooltips and popover windows, both modal and regular. Each type of window comes with its own JavaScript.

### Working with JavaScript

Generally speaking, Bootstrap looks and works quite well on its own, but if desired, it's easy to add interaction with a site created based on it from JavaScript. Bootstrap comes with ready-made examples of JS code that can be extended and customized for your needs. The supplied plugins work in conjunction with [jQuery](http://jquery.com/) and [Ender](http://ender.no.de/).

### Bottom Line

If you, like me, sometimes need to do layout but you don't do it professionally and don't plan to, it makes sense to look at [Twitter Bootstrap](http://twitter.github.com/bootstrap/) - it can serve as a good starting point for laying out a project. At the same time, there won't be that feeling that the site markup was done by a back-end programmer :)
But if you want to learn how to do layout and are looking for where to start - read [Ivan Sagalaev's series of articles](http://softwaremaniacs.org/blog/category/primer/) on the basics of block layout.

By the way, I also initially wanted to make this site using Bootstrap, but in the end I decided to try another CSS framework - [Gumby](http://www.gumbyframework.com/).
