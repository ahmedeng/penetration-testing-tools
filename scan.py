#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import shlex
import os
import errno
import uuid
import re

from urlparse import urlsplit


#Start of class Scanner

class UrlsFile:

    def __init__(self):
        self.utils=Utils()
        
        
    

    


    def start_scan_by_file(targets_file):
        target_url=""
        line_num=1
        with open(targets_file) as f:
            for line in f:
                if session_name!="":
                    if session["opt"]=="load":
                        if line_num < session["line"]:
                            line_num=line_num+1
                            continue
                    
                    session["line"]=line_num
                    save_session()
                    line_num=line_num+1
                    print session["line"]
                        
                result = re.search("(?P<url>https?://[^\s]+)", line)
                if result:
                    target_url=result.group("url")
                    start_scan_by_url(target_url)
        
    
