#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt
import os
import errno

def create_save_dir(path):
    try:
        os.makedirs(path)
        
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    if path[-1] != '/':
        path=path+'/'

    return path   

def find_injected(dir):
    import csv
    targets=[]
    i=0
    if dir[-1] != '/':
        dir=dir+'/'

    injectable_dir=create_save_dir(dir+'injectable')
    for root, dirs, files in os.walk(dir):
        if injectable_dir not in root:            
            for file in files:
                if file == "log":
                    log_file_path=os.path.join(root,file)
                    log_file_size=os.path.getsize(log_file_path)
                    if log_file_size > 0:
                        #with open(log_file_path, 'r') as log_file:
                            #for line in log_file:
                                #if 'available databases' in line:
                        target={}
                        target_file_path=os.path.join(root,'target.txt')
                        with open(target_file_path, 'r') as target_file:
                            injection_point = target_file.readline().split()[0]
                        target_file
                        i=i+1
                        target['host']=os.path.basename(os.path.dirname(log_file_path))
                        target['injection_point']=injection_point
                        target['type']='sql injection'
                        target['tool']='sql_map'
                        targets.append(target)
                        print str(i)+"-"+log_file_path
                        os.system('mv -f '+root+' '+injectable_dir)
                                #break
    #print targets


    
    if len(targets):
        targets_file = open('targets.csv', 'wb')
        keys=targets[0].keys()
        dict_writer = csv.DictWriter(targets_file, keys)
        dict_writer.writer.writerow(keys)
        dict_writer.writerows(targets)


def main(argv):
   print argv  
   find_injected(argv[0])
                
if __name__ == "__main__":
   main(sys.argv[1:])
