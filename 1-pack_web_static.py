#!/usr/bin/python3
# Fabric script that generates a .tgz archive from
# the contents of the web_static
from time import strftime
from fabric.api import *


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    set_up = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(set_up))
        return("versions/web_static_{}.tgz".format(set_up))
    except:
        return(None)
