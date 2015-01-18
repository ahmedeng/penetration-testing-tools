#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import errno
import urllib
from urlparse import urlsplit


COMMENT_CHAR = '#'
OPTION_CHAR =  '='

#Start of class Utils

class Utils:


    def parse_config(self,filename):
        options = {}
        
         
        with open(filename) as f:
            for line in f:
                # First, remove comments:
                if COMMENT_CHAR in line:
                    # split on comment char, keep only the part before
                    line, comment = line.split(COMMENT_CHAR, 1)
                # Second, find lines with an option=value:
                if OPTION_CHAR in line:
                    # split on option char:
                    option, value = line.split(OPTION_CHAR, 1)
                    # strip spaces:
                    option = option.strip()
                    value = value.strip()
                    # store in dictionary:
                    options[option] = value
        return options

    

    def fix_url(self,url):
        if "http://" not in url:
            if "https://" not in url:
                url="http://"+url
        return urllib.unquote(url).replace('"','')
        #return url

    def create_save_dir(self,path):
        try:
            os.makedirs(path)
            
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        path=os.path.abspath(path)
        if path[-1] != '/':
            path=path+'/'

        return path

    def get_host(self,url):
        #print url
        host = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
        #print(host)
        return host

    
