#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import requests
import socket
import sys
import time
from twisted.python import filepath
import urlparse

from bs4 import BeautifulSoup
import sqlite3 as lite
import utils


google_domains=".google.com .google.ad .google.ae .google.com.af .google.com.ag .google.com.ai .google.al .google.am \
.google.co.ao .google.com.ar .google.as .google.at .google.com.au .google.az .google.ba .google.com.bd .google.be .google.bf \
.google.bg .google.com.bh .google.bi .google.bj .google.com.bn .google.com.bo .google.com.br .google.bs .google.bt .google.co.bw \
.google.by .google.com.bz .google.ca .google.cd .google.cf .google.cg .google.ch .google.ci .google.co.ck .google.cl .google.cm \
.google.cn .google.com.co .google.co.cr .google.com.cu .google.cv .google.com.cy .google.cz .google.de .google.dj .google.dk \
.google.dm .google.com.do .google.dz .google.com.ec .google.ee .google.com.eg .google.es .google.com.et .google.fi \
.google.com.fj .google.fm .google.fr .google.ga .google.ge .google.gg .google.com.gh .google.com.gi .google.gl .google.gm \
.google.gp .google.gr .google.com.gt .google.gy .google.com.hk .google.hn .google.hr .google.ht .google.hu .google.co.id \
.google.ie .google.co.il .google.im .google.co.in .google.iq .google.is .google.it .google.je .google.com.jm .google.jo \
.google.co.jp .google.co.ke .google.com.kh .google.ki .google.kg .google.co.kr .google.com.kw .google.kz .google.la \
.google.com.lb .google.li .google.lk .google.co.ls .google.lt .google.lu .google.lv .google.com.ly .google.co.ma .google.md \
.google.me .google.mg .google.mk .google.ml .google.com.mm .google.mn .google.ms .google.com.mt .google.mu .google.mv \
.google.mw .google.com.mx .google.com.my .google.co.mz .google.com.na .google.com.nf .google.com.ng .google.com.ni .google.ne \
.google.nl .google.no .google.com.np .google.nr .google.nu .google.co.nz .google.com.om .google.com.pa .google.com.pe \
.google.com.pg .google.com.ph .google.com.pk .google.pl .google.pn .google.com.pr .google.ps .google.pt .google.com.py \
.google.com.qa .google.ro .google.ru .google.rw .google.com.sa .google.com.sb .google.sc .google.se .google.com.sg .google.sh \
.google.si .google.sk .google.com.sl .google.sn .google.so .google.sm .google.sr .google.st .google.com.sv .google.td \
.google.tg .google.co.th .google.com.tj .google.tk .google.tl .google.tm .google.tn .google.to .google.com.tr .google.tt \
.google.com.tw .google.co.tz .google.com.ua .google.co.ug .google.co.uk .google.com.uy .google.co.uz .google.com.vc \
.google.co.ve .google.vg .google.co.vi .google.com.vn .google.vu .google.ws .google.rs .google.co.za .google.co.zm \
.google.co.zw .google.cat".split()


class UrlGoogle:
    def __init__(self,query,domain='com',results_count=100,start_page=1,end_page=1):
        self.query=query
        self.start_page=start_page
        self.end_page=end_page
        #self.host='http://www.google.'+domain
        #self.search_link=self.host
        self.urls=set()
        self.next_domain=0
        self.results_count=results_count
        
        
    def search(self):
        retry=True
        same_result_threshold=7
        prev_result_length=0
        threshold=0
        while retry:
            if self.next_domain==len(google_domains):
                return False
            google_domain = google_domains[self.next_domain]
            google_domain='http://www'+google_domain
            search_link=google_domain+"/search?num="+str(self.results_count)+"&q="+self.query+"&oq="+self.query+"&aqs=chrome..69i57.1384j0j9&sourceid=chrome&es_sm=93&ie=UTF-8"
            print '########################################\n'+str(len(google_domains))+'-'+str(self.next_domain)+'-'+search_link+'\n########################################'
            try:
                responce=requests.get(search_link,timeout=20)
                print 'HTTP code:'+str(responce.status_code)
                if responce.status_code==200:
                    #print 'CCC'
                    data=responce.text
                    #print 'CCCCCCCCCC'
                elif responce.status_code==503:
                    if len(self.urls):
                        return True
                    else:
                        print time.strftime("%H:%M:%S", time.localtime())+" -- Sleeping a while ..."
                        time.sleep(900)
                        self.next_domain=self.next_domain+1
                        continue
                else:
                    self.next_domain=self.next_domain+1
                    continue
            except (requests.exceptions.Timeout,requests.exceptions.ConnectionError,socket.error):
                continue
            #print page    
            soup=BeautifulSoup(data)
            #print soup.prettify()
            for li in soup.find_all('li',attrs={'class':'g'}):
                url=li.a['href']
                url=urlparse.parse_qs(urlparse.urlparse(url).query)
                if 'q' in url:
                    url=url['q'][0]
                    self.urls.add(url)

            print 'Urls found:'+str(len(self.urls))

            if not len(self.urls):
                return False
            else:
                self.next_domain=self.next_domain+1
                if not prev_result_length:
                    prev_result_length=len(self.urls)
                    
                else:
                    if len(self.urls) == prev_result_length:
                        threshold=threshold+1
                    else:
                        prev_result_length=len(self.urls)
                        #threshold=0
                if threshold==same_result_threshold:
                    break
                
        return True
            #time.sleep(3)

    def retry(self):
        self.search()


    def save(self,filepat,out_dir):
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'+'\n'.join(self.urls)+'\n Total Urls found:'+str(len(self.urls))+'\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        
        os.system('cp -f urls/urls.db '+out_dir+'/urls.db')
        con = lite.connect('urls/urls.db')

        with con:    
            cur = con.cursor() 
            utils=utils.Utils()   
            for item in self.urls:
                global utils
                host=utils.get_host(item)
                cur.execute("SELECT host FROM urls where ='" + host+"'")                
                data = cur.fetchone()
                if not data:
                    cur.execute("INSERT INTO urls VALUES('"+host+"','"+item+"')")

        with open(filepath, 'w') as file:
            for item in self.urls:
               file.write("{}\n".format(item))
        

##u=UrlGoogle('site:.il','co.il')
##u.search()
##print '\n'.join(u.urls)+'\n'+str(len(u.urls))
