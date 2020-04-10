#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
import os
from fabric.api import *
from datetime import datetime

env.user = "ubuntu"
env.hosts = ['34.74.118.58', '54.234.179.10']


def do_deploy(archive_path):
    """distributes between 2 servers"""
    if not path.isfile(archive_path):
        return False

    route = archive_path.split('/')[1]
    my_dir = "/data/web_static/releases/" + route
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(my_dir))
        run("sudo tar -xzf /tmp/{} -C {}/".format(route, my_dir))
        run("sudo rm /tmp/{}".format(route))
        run("sudo mv {}/web_static/* {}/".format(my_dir, my_dir))
        run("sudo rm -rf {}/web_static".format(my_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(my_dir))
        print("New version deployed")
        return True
    except:
        return False
