#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import shlex
import os
import errno
import uuid
import re

import urllib
from urlparse import urlsplit


#Start of class Scanner

class Scanners:

    def __init__(self):
        self.utils=Utils()
        self.scanners = {}
        
        
    

    def load_scanners(self):
        global scanners

        for filename in os.listdir(SCANNERS_DIR):
            #print  filename
            command_line_name = filename
            options = parse_config(SCANNERS_DIR+filename)
            scanners[command_line_name]=options["command_options"]
            
            #create_save_dir(save_dir+command_line_name)
    
