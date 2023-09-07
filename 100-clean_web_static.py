#!/usr/bin/python3
""" Removes out if date archives."""
from fabric.api import cd, env, lcd, local, run

env.hosts = ['18.204.10.209', '52.87.230.171']


def do_clean(number=0):
    """ Removesoutdated archives. """

    try:
        number = int(number)
        number >= 0

    except:
        return None

    number = 2 if number <= 1 else number + 1

    with lcd("./versions"):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number))
    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))
