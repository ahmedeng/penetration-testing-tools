#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt

# import urls

import scanners
import groups
import session
import config
import scanurl
import urlsfile
import urlsdorksfile
import urlsdorks

# Start of class R4bia

class R4bia:
    def __init__(self):
        
        self.scanners = scanners.Scanners()
        self.groups = groups.Groups()
        self.session = session.Session()       
                  
        self.global_vars = {'requested_scanners_string':"all",
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
                   'save_dir':config.CURRENT_DIR + "/output/",
                   'dorks_country':"",
                   'next_url':False,
                   'delete_file':False,
                   'db_file':False,
                   'advanced_search_url':"",
                    }

        self.flags = {'uflag':False,
                    'fflag':False,
                    'dorks_flag':False,
                    'dorks_file_flag':False,
                    'sflag':False,
                    'save_dir_flag':False
                    }
         
        
    def usage(self):
        logo = """
    ,,,.,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,.,,,
    ,:@:.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,,,,.,#;,
    .@.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@;,,,,,,,,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,,.'',,,,,,,,.#@@@@;,,,,,,,,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,,,,,,,@@@@+,,,,,,,@@@@@:,,,,,,,+@@@,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,,@@@@@.,,,,,;@@@@@,,,,,,.@@@@@.,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,.@@@@@',,,,,#@@@@@.,,,,.@@@@@;,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,::.,,:,,,,#@@@@@.,,,.@@@@@@.,,,.@@@@@#,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,;@@@;,,,,,,+@@@@@',,,:@@@@@@.,,.@@@@@@.,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,'@@@#.,,,,;@@@@@@.,,#@@@@@@.,.@@@@@@,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,#@@@@,,,,:@@@@@@#..@@@@@@@..@@@@@#;,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,.@@@@@;,,.@@@@@@@'.@@@@@@#`@@@@@@+,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,@@@@#',.@@@@@@@@@@@@@@@@@@@@@@@.,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,:@@@@@+.@@@@@@@@@@@@@@@@@@@@@@#,,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,+#@@@@@@@@@@@##++;,,'@@@'`+@@#,,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,.@@@@@@@@@@;'@@@@@@@@@@@@##`;#,,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,,+@@@@@@@@@@#.'#@@#+',,#@@@@'.,,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,:,@@@@@@@@@@@@`#@@@@@@@@@@@@@@.,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,,.#@@@@@@@@@@''@@@@@@@@@@@@@@@#,,,,,,,,,,,,,,,,.#:
    .@.,,,,,,,,,,,,,,,,,@@@@@@@@@@;#@@@@@@@@@@@@@@@',,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,+@@@@@@@@@@;#@@@@@@@@@@@@@#,,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,.#@@@@@@@@@@+@@@@@@@@@@@@#,,,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,'@@@@@@@@@@#@@@@@@@@@#,,,,,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,,.++#@@###++#@+#@+#@,,,,,,,,,,,,,,,,,,,,,,.#,
    .@.,,,,,,,,,,,,,,,,,,,,,,#.@+,:+`@.+`+':.;,,,,,,,,,,,,,,,,,,,,,,.#:
    .#',,,,,,,,,,,,,,,,,,,,,,;.#.;:+.+.#.+,+.,,,,,,,,,,,,,,,,,,,,,,,;#.
    ,,,'###################:,#.##;:+,,.#`+`#::#####################+,,,

        """
        print logo
        return

        
    

    def start(self):

        # config.set_config_drrectories()
        self.groups.load_groups()
        self.scanners.load_scanners()
        # print self.scanners.scanners
        
        if self.global_vars['requested_scanners_string'] == "all":
            self.global_vars['requested_scanners_string'] = ""
            for scan in self.scanners.scanners.keys():
                self.global_vars['requested_scanners_string'] = self.global_vars['requested_scanners_string'] + scan + ','
            self.global_vars['requested_scanners_string'] = self.global_vars['requested_scanners_string'][:-1]
            # print requested_scanners_string
        if self.global_vars['proxychains_string'] == "all":
             self.global_vars['proxychains_string'] = ""
             for scan in self.scanners.scanners.keys():
                 self.global_vars['proxychains_string'] = self.global_vars['proxychains_string'] + scan + ','
             self.global_vars['proxychains_string'] = self.global_vars['proxychains_string'][:-1]

        if self.global_vars['requested_groups_string'] in self.groups.groups.keys():
            self.global_vars['requested_scanners_string'] = self.groups[self.global_vars['requested_groups_string']]
        
        self.session.start_session(self.global_vars) 
        if self.flags['uflag']:
          # print self.global_vars
          _scanurl = scanurl.ScanUrl()
          _scanurl.start_scan_by_url(self.global_vars, self.scanners.scanners, self.session)
        elif self.flags['fflag']:
          _urlsfile = urlsfile.UrlsFile()        
          _urlsfile.start_scan_by_file(self.global_vars, self.scanners.scanners, self.session)
        elif self.flags['dorks_file_flag']:
          _urlsdorksfile = urlsdorksfile.UrlsDorksFile()
          _urlsdorksfile.start_scan_by_dorks_file(self.global_vars, self.scanners.scanners, self.session)
        elif self.flags['dorks_flag']:
          _urlsdorks = urlsdorks.UrlsDorks()
          _urlsdorks.start_scan_by_dorks(self.global_vars, self.scanners.scanners, self.session)
        elif self.flags['sflag']:
          self.session.load_session(self.global_vars)
        else:
          print 'scan_web.py -f <outputfile>'
          return
       
         
         
        
def main(argv):

   
   gflag = False
   
   r4bia = R4bia()
   r4bia.usage()   

   try:
      opts, args = getopt.getopt(argv, "ho:f:u:s:g:p:td:a:", ["advanced_search_url=","db","delete_file", "next_url", "goodork", "add_options=", "session=", "dorks_file=", "dorks=", "demo", "proxychains=", "groups=", "scanners=", "save_dir=", "file=", "url=", "dorks_country="])
   except getopt.GetoptError:
      print 'scan_web.py -f <outputfile>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-f", "--file"):
         r4bia.global_vars['targets_file'] = arg
         r4bia.flags['fflag'] = True
      elif opt in ("-u", "--url"):
         r4bia.global_vars['target_url'] = arg
         r4bia.flags['uflag'] = True
      elif opt in ("-o", "save_dir"):
         r4bia.global_vars['save_dir'] = arg
         r4bia.flags['save_dir_flag'] = True 
      elif opt in ("-g", "--groups"):
         r4bia.global_vars['requested_groups_string'] = arg
         gflag = True
      elif opt == "--dorks_country":
         r4bia.global_vars['dorks_country'] = arg
      elif opt == "--advanced_search":
         r4bia.global_vars['advanced_search_url'] = arg
         print r4bia.global_vars["advanced_search_url"]
                
               
      elif opt in ("-s", "--scanners"):
         if not gflag:
             r4bia.global_vars['requested_scanners_string'] = arg
      elif opt in ("-p", "--proxychains"):
         r4bia.global_vars['proxychains_string'] = arg
      elif opt in ("-t", "--demo"):
         r4bia.global_vars['tflag'] = True
      elif opt == "--dorks_file":
         r4bia.flags['dorks_file_flag'] = True
         r4bia.global_vars['dorks_file'] = arg
      elif opt in ("-d", "--dorks"):
         r4bia.flags['dorks_flag'] = True
         r4bia.global_vars['dorks'] = arg
      elif opt == "--session":
        r4bia.global_vars['session_name'] = arg
        r4bia.flags['sflag'] = True
      elif opt == "--goodork":
        r4bia.global_vars['goodork_flag'] = True
      elif opt == "--next_url":
        r4bia.global_vars['next_url'] = True
      elif opt == "--db":
        r4bia.global_vars['db_file'] = True
      elif opt == "--delete_file":
        r4bia.global_vars['delete_file'] = True
      elif opt in ("-a", "--add_options"):
        r4bia.global_vars['add_options_string'] = arg
         
      

   
   r4bia.start()                          
   
          
   
if __name__ == "__main__":
   main(sys.argv[1:])


