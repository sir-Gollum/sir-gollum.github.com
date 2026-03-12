+++
date = '2012-08-04T22:30:00+02:00'
draft = false
title = 'Virtualenv'
tags = ['tools', 'python']
type = "posts"
+++


Есть куча способов установки питоновских пакетов. Какие-то более удобны, какие-то менее, в зависимости от ситуации. Опишу способ, который мне оказался удобен в большинстве случаев.

Для его использования не нужно ничего, кроме собственно [virtualenv](https://virtualenv.pypa.io/en/latest/) и [pip](https://pypi.org/project/pip/). Для каждого проекта я использую отдельную среду со своим набором пакетов - мне так удобнее управлять зависимостями.

Для создания окружений я использую небольшую функцию в `~/.profile`:

```bash
mkenv() {
  VENV_PATH="$HOME/.python-envs`pwd`"
  virtualenv --no-site-packages -p `which python` $VENV_PATH
  echo "VIRTUALENV_PATH=$VENV_PATH" > .venv
  source $VENV_PATH/bin/activate
}
```

Окружения создаются в скрытой папке `~/.python-envs/<путь_к_папке_с_проектом>`, а путь к окружению пишется в папку проекта в скрытый файл `.venv`. В принципе, путь можно и вычислять, но я уже пару раз менял место для новых окружений, а так нет необходимости переносить старые.

Далее, хотелось бы как-то автоматически активировать окружение, когда мы начинаем работать с проектом. Для этой цели я использую еще один скрипт, лежащий в `~/.profile` и проверяющий как раз файлы `.venv`. Скрипт срабатывает, когда изменилась текущая директория.

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

Вот собственно и всё. Какие это даёт удобства:

- не надо ставить еще что-то, например [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
- легко отслеживать зависимости с помощью pip, легко увидеть набор пакетов, нужных конкретному проекту
- окружения включаются и выключаются автоматически тогда, когда они нужны

Чтобы не тянуть пакеты из сети каждый раз, когда они нужны, а также на случай падения [pypi](http://pypi.python.org) или атомной войны, можно еще добавить сюда использование [PIP_DOWNLOAD_CACHE](http://stackoverflow.com/questions/4806448/how-do-i-install-from-a-local-cache-with-pip) и [collective.eggproxy](http://pypi.python.org/pypi/collective.eggproxy/).
