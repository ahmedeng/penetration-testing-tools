#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import utils
import config


#Start of class Groups

class Groups:

    def __init__(self):
        self.utils=utils.Utils()
        self.groups = {}
        

    
    def load_groups(self):
        
        for filename in os.listdir(config.GROUPS_DIR):
            group_name = filename
            options = self.utils.parse_config(config.GROUPS_DIR+filename)
            self.groups[group_name]=options["scanners"]
            
        return
        
