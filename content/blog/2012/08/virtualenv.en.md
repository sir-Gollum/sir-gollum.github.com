+++
date = '2012-08-04T22:30:00+02:00'
draft = false
title = 'Virtualenv'
tags = ['tools', 'python']
type = "posts"
+++

There are tons of ways to install Python packages. Some are more convenient, some less so, depending on the situation. I'll describe the approach that I've found most convenient in the majority of cases.

To use it, you don't need anything except [virtualenv](https://virtualenv.pypa.io/en/latest/) and [pip](https://pypi.org/project/pip/) themselves. <!--more-->For each project, I use a separate environment with its own set of packages - I find it easier to manage dependencies this way.

To create environments, I use a small function in `~/.profile`:

```bash
mkenv() {
  VENV_PATH="$HOME/.python-envs`pwd`"
  virtualenv --no-site-packages -p `which python` $VENV_PATH
  echo "VIRTUALENV_PATH=$VENV_PATH" > .venv
  source $VENV_PATH/bin/activate
}
```

Environments are created in the hidden folder `~/.python-envs/<path_to_project_folder>`, and the path to the environment is written to the project folder in a hidden `.venv` file. In principle, you could calculate the path, but I've already changed the location for new environments a couple of times, and this way there's no need to move the old ones.

Next, I wanted to somehow automatically activate the environment when I start working with a project. For this purpose, I use another script in `~/.profile` that checks for those `.venv` files. The script triggers when the current directory changes.

```bash
PREVPWD=`pwd`
PREVENV_PATH=
PREV_PS1=
PREV_PATH=

handle_virtualenv(){
  if [ "$PWD" != "$PREVPWD" ]; then
    PREVPWD="$PWD";
    if [ -n "$PREVENV_PATH" ]; then
      if [ "`echo "$PWD" | grep -c $PREVENV_PATH`" = "0"  ]; then
         source $PREVENV_PATH/.venv
         echo "> Virtualenv `basename $VIRTUALENV_PATH` deactivated"
         PS1=$PREV_PS1
         PATH=$PREV_PATH
         PREVENV_PATH=
      fi
    fi
    if [ -e "$PWD/.venv" ] && [ "$PWD" != "$PREVENV_PATH" ]; then
      PREV_PS1="$PS1"
      PREV_PATH="$PATH"
      PREVENV_PATH="$PWD"
      source $PWD/.venv
      echo $VIRTUALENV_PATH
      source $VIRTUALENV_PATH/bin/activate
      echo "> Virtualenv `basename $VIRTUALENV_PATH` activated"
    fi
  fi
}

export PROMPT_COMMAND=handle_virtualenv
```

And that's basically it. So, what are the benefits?

- No need to install anything extra, like [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html).
- It's easy to track dependencies with pip and see the exact set of packages needed for a specific project.
- Environments are activated and deactivated automatically, right when you need them.

To avoid fetching packages from the network every time, and also in case [PyPI](http://pypi.python.org/) goes down or a nuclear war breaks out, you can also add [PIP_DOWNLOAD_CACHE](https://stackoverflow.com/questions/4806448/how-do-i-install-from-a-local-cache-with-pip) and [collective.eggproxy](https://pypi.org/project/collective.eggproxy/) to the mix.
