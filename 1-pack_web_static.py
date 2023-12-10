#!/usr/bin/python3
"""This Fabric script generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack."""
import os
from datetime import datetime
from fabric.api import local, runs_once

@runs_once
def do_pack():
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    curr_time = datetime.now()
    formatted_date = curr_time.strftime("%Y%m%d%H%M%S")

    filename = "versions/web_static_{}.tgz".format(formatted_date)
    print("Packing web_static to {}".format(filename))
    result = local("tar -cvzf {} web_static".format(filename))
    size = os.stat(filename).st_size
    print("web_static packed: {} -> {}Bytes".format(filename, size))
    if result.succeeded:
        return filename
    else:
        return None
