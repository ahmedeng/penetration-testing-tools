#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import shlex
import os
import errno
import uuid
import re
import utils


#Start of class Scanner

class ScanUrl:

    def __init__(self):
        self.utils=utils.Utils()
        
        
    

    


    def start_scan_by_url(self,global_vars,scanners,session):

        url=self.utils.fix_url(global_vars['target_url'])
        
        host = self.utils.get_host(url)
        
        
        scans=global_vars['requested_scanners_string'].split(",")
        print scans
        for scan in scans:
            if global_vars['session_name']!="":
                if session.session["opt"]=="load":
                    if session.session["scan"]:
                        if scans.index(session.session["scan"]) > scans.index(scan):
                            continue
                        
                session.session["scan"]=scan
                session.save_session()
                
            #print scan
            #print scanners
            output_dir=self.utils.create_save_dir(global_vars['save_dir']+host.replace("/",""))
            
            if scan in scanners.keys():

                if '_' in scan:
                    command_name=scan.split("_")[0]
                else:
                    command_name=scan

                output_option=False

                output_dir=self.utils.create_save_dir(global_vars['save_dir']+host.replace("/","")+"/"+command_name)
                #output_dir=save_dir+scan
                output_file=output_dir+host.replace("/","");
                #print output_file
                command= command_name+" "+scanners[scan]+" "+global_vars['add_options_string']

                if scan in global_vars['proxychains_string']:
                    command= "proxychains "+command
                if "{url}" in command:
                        command=command.replace("{url}",url)
                if "{output_file}" in command:
                    command=command.replace("{output_file}",output_file)
                    output_option=True
                if "{output_dir}" in command:
                    #output_dir=create_save_dir(output_dir+host.replace("/",""))
                    command=command.replace("{output_dir}",output_dir)
                    output_option=True
                
                print command
                
                if not global_vars['tflag']:
                    subprocess.call(shlex.split(command),shell=False)
    ##                if output_option:
    ##                    subprocess.call(shlex.split(command),shell=False)
    ##                    #os.system(command)
    ##                else:
    ##                   # command=command+" 1>&2 exit 1"
    ##                    #print command
    ##                   
    ##                    os.system(command)
    ##                    #out=subprocess.check_output(['wafw00f','rehaby.net']);
    ####                    p=subprocess.Popen(command.split(),shell=False,stdout=subprocess.PIPE);
    ####                    output, err = p.communicate();
    ####                    text_file = open(output_file+".txt", "w")
    ####                    text_file.write(output)
    ####                    text_file.close()
    ##                
    ##                
            else:
                print "Undefined scanner"
            
        session.session["scan"]=""
        session.save_session()
        return

