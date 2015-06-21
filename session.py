#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle as pickle
import config
import scanners
import scanurl
import urlsfile
import urlsdorksfile



#Start of class Session

class Session:

    def __init__(self):
        self.session={'requested_scanners_string':"all",
                   'requested_groups_string':"",
                   'proxychains_string':"",
                   'add_options_string':"",
                   'session_name':"",              
                   'add_options_string':"",        
                   'tflag':False,
                   'goodork_flag':False,
                   'dork':"",
                   'target_url':"",
                   'targets_file':"",
                   'dorks_file':"",
                   'save_dir':config.CURRENT_DIR+"/output/",
                   'dorks_country':"",
                   'db_file':False,
                   'advanced_search_url':"",
                    }

        



    def save_session(self):
        pickle.dump( self.session, open( config.SESSIONS_DIR+self.session["session_name"], "wb" ) )
        
    def start_session(self,global_vars):
        print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
        self.session["requested_scanners_string"]=global_vars['requested_scanners_string']
        self.session["proxychains_string"]=global_vars['proxychains_string']
        self.session["target_url"]=global_vars['target_url']
        self.session["targets_file"]=global_vars['targets_file']
        self.session["dorks_file"]=global_vars['dorks_file']
        self.session["save_dir"]=global_vars['save_dir']
        self.session["dorks_country"]=global_vars['dorks_country']
        self.session["opt"]="start"
        self.session["session_name"]=global_vars['session_name']
        self.session = pickle.load( open( config.SESSIONS_DIR+global_vars['session_name'], "rb" ) )
        self.session["db_file"]=global_vars['db_file']
        self.session["advanced_search_url"]=global_vars['advanced_search_url']
        pickle.dump( self.session, open( config.SESSIONS_DIR+self.session["session_name"], "wb" ) )
        exit()
        #print session
        return

    def load_session(self,global_vars):
        
        self.session = pickle.load( open( config.SESSIONS_DIR+global_vars['session_name'], "rb" ) )
        self.session["opt"]="load"
        #print session

##        requested_scanners_string=self.session["requested_scanners_string"]
##        proxychains_string=self.session["proxychains_string"]
##        save_dir=self.session["save_dir"]    
        _scanners=scanners.Scanners()
        _scanners.load_scanners()
        if self.session["target_url"]!="":
            if self.session["scan"]:
                if not global_vars['next_url']:
                    _scanurl=scanurl.ScanUrl()
                    _scanurl.start_scan_by_url(self.session,_scanners.scanners,self)
                if self.session["targets_file"]!="":
                    self.session["urls_line"]=self.session["urls_line"]+1
        if self.session["targets_file"]!="":
            _urlsfile=urlsfile.UrlsFile()        
            _urlsfile.start_scan_by_file(self.session,_scanners.scanners,self)
        if self.session["dorks_file"]!="":
            _urlsdorksfile=urlsdorksfile.UrlsDorksFile()
            _urlsdorksfile.start_scan_by_dorks_file(self.session,_scanners.scanners,self)
        
        
