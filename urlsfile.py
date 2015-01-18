#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
import re
import scanurl

#Start of class Scanner

class UrlsFile:

    
    def start_scan_by_file(self,global_vars,scanners,session):
        target_url=""
        line_num=1
        with open(global_vars['targets_file']) as f:
            for line in f:
                if global_vars['session_name']!="":
                    if session.session["opt"]=="load":
                        if line_num < session.session["urls_line"]:
                            line_num=line_num+1
                            continue
                    
                    session.session["urls_line"]=line_num
                    session.save_session()
                    line_num=line_num+1
                    print session.session["urls_line"]
                        
                result = re.search("(?P<url>https?://[^\s]+)", line)
                if result:
                    global_vars['target_url']=result.group("url")
                    _scanurl=scanurl.ScanUrl()
                    _scanurl.start_scan_by_url(global_vars,scanners,session)
        print 'End of urls file.'
        print str(line_num)+' urls scanned'
                    
                    
    
