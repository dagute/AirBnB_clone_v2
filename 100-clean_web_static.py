#!/usr/bin/python3
"""Keep it clean"""

from fabric.api import *

env.hosts = ['104.196.221.76', '54.234.179.10']
env.user = 'ubuntu'


def do_clean(number=0):
    number = int(number)
    """Clean everything"""
    with lcd('versions'):
        if number == 0 or number == 1:
            local('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            local('ls -t | tail -n +{} | xargs rm -rfv'.format(number + 1))
    with cd('/data/web_static/releases/'):
        if number == 0 or number == 1:
            run('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            run('ls -t | tail -n +{} | xargs rm -rfv'.format(number + 1))
