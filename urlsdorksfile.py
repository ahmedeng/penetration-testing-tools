#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import uuid
import urlsdorks
import urlsfile



#Start of class Scanner

class UrlsDorksFile:

    
    def start_scan_by_dorks_file(self,global_vars,scanners,session):
        line_num=1
        #print global_vars['dorks_file']
        if os.path.isfile(global_vars['dorks_file']):
##            demo=False
##            if not global_vars['tflag']:
##                global_vars['tflag']=True
##                demo=True
##            output_files=[]
            with open(global_vars['dorks_file']) as f:
                for dork in f:
                    if global_vars['session_name']!="":
                        if session.session["opt"]=="load":
                            if line_num < session.session["dorks_line"]:
                                line_num=line_num+1
                                continue
                        
                        session.session["dorks_line"]=line_num
                        session.save_session()
                        line_num=line_num+1
                        print session.session["dorks_line"]
                            
                    global_vars['dorks']=dork.replace('\n','')
                    _urlsdorks=urlsdorks.UrlsDorks()
                    output_filename=_urlsdorks.start_scan_by_dorks(global_vars,scanners,session)
                    session.session["dorks_line"]=line_num+1
                    session.save_session()
                    if output_filename != "":
                        if not global_vars['tflag']:
                            session.session["urls_line"]=1
                            session.save_session()
        
                            global_vars['targets_file']=output_filename
                            _urlsfile=urlsfile.UrlsFile()        
                            _urlsfile.start_scan_by_file(global_vars,scanners,session)
                        
                    #print output_file
                    #output_files.append(output_file)

            #print output_files
##            if output_files:
##                output_filename=global_vars['save_dir']+"urls/"+str(uuid.uuid4())+".urls"
##                command =" "
##                command=command.join(output_files)
##                command="cat "+command+" >> "+output_filename
##                print command
##                os.system(command)
##                #subprocess.Popen(command,shell=False);
##                if demo:
##                    global_vars['tflag']=False
##                if os.path.isfile(output_filename):
##                    global_vars['targets_file']=output_filename
##                    _urlsfile=urlsfile.UrlsFile()        
##                    _urlsfile.start_scan_by_file(global_vars,scanners,session)
        return





    def start_scan_by_dorks(dorks):
        if goodork_flag:
            options = parse_config(GOODORK_DIR+"goodork")
            goodork_path=options["path"]
            output_filename=GOODORK_DIR+"output/"+str(uuid.uuid4())
            command=goodork_path+" "+dorks+" -o "+output_filename
            print command
            subprocess.call(command.split(),shell=False);
        else:
            output_dir=create_save_dir(save_dir+"urls")
            output_filename=output_dir+str(uuid.uuid4())
            u=urls.UrlGoogle('site:.il inurl:'+dorks,'co.il')
            u.search()
            u.save(output_filename)
        if os.path.isfile(output_filename):
            if not tflag:
                start_scan_by_file(output_filename)
        
            return output_filename
        return ""


