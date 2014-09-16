#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import utils
import config


#Start of class Scanners

class Scanners:

    def __init__(self):
        self.utils=utils.Utils()
        self.scanners = {}
        
        
    

    def load_scanners(self):
        
        for filename in os.listdir(config.SCANNERS_DIR):
            #print  filename
            command_line_name = filename
            options = self.utils.parse_config(config.SCANNERS_DIR+filename)
            self.scanners[command_line_name]=options["command_options"]
            
            #create_save_dir(save_dir+command_line_name)
    
