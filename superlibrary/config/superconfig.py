# AUTHOR: nmacatangay

import os
from configparser import ConfigParser

"""
TO USE THIS, CREATE A "config_files" FOLDER IN YOUR
APPLICATIONS' ROOT DIRECTORY

APP_DIRECTORY
 |- <config_files>
  |- config1.conf
  |- config2.conf
 |- main_script.py
"""

def get_config(config_name):

    # DEFINE FILEPATH
    filepath = "%s/config_files/%s" % (os.getcwd(), config_name)

    # INTIALIZE CONFIG PARSER
    config_file = ConfigParser()

    # READ CONFIG FILE
    config_file.read(filepath)

    return config_file
