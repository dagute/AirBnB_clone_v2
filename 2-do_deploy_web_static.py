#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from time import strftime
from fabric.api import *
import os.path

env.user = "ubuntu"
env.hosts = ['104.196.221.76', '54.234.179.10']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    set_up = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(set_up))
        return("versions/web_static_{}.tgz".format(set_up))
    except:
        return(None)


def do_deploy(archive_path):
    """distributes between 2 servers"""
    if (os.path.isfile(archive_path) is False):
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
