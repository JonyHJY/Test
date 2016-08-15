#!/usr/bin/env python 
#-*- coding: utf-8 -*- 
#ͨ��urllib(2)ģ�������������� 
import urllib,urllib2,gevent 
#����������ʽģ�飬ʱ��ģ�� 
import re,time 
from gevent import monkey 
    
monkey.patch_all() 
    
def geturllist(url): 
    url_list=[] 
    print url
    req_timeout = 1	
    s = urllib2.urlopen(url,req_timeout) 
    text = s.read() 
    #����ƥ�䣬ƥ�����е�ͼƬ 
    html = re.search(r'<ol.*</ol>', text, re.S) 
    urls = re.finditer(r'<p><img src="(.+?)jpg" /></p>',html.group(),re.I) 
    for i in urls: 
        url=i.group(1).strip()+str("jpg") 
        url_list.append(url) 
    return url_list 
    
def download(down_url): 
    name=str(time.time())[:-3]+"_"+re.sub('.+?/','',down_url) 
    print name 
    urllib.urlretrieve(down_url, "E:\\TEMP\\"+name) 
    
def getpageurl(): 
    page_list = [] 
    #�����б�ҳѭ�� 
    for page in range(2000,2002): 
        url="http://jandan.net/ooxx/page-"+str(page)+"#comments"
        #�����ɵ�url���뵽page_list�� 
        page_list.append(url) 
    print page_list 
    return page_list 
if __name__ == '__main__': 
    jobs = [] 
    pageurl = getpageurl()[::-1] 
    #����ͼƬ����  
    for i in pageurl: 
        for (downurl) in geturllist(i): 
            jobs.append(gevent.spawn(download, downurl)) 
    gevent.joinall(jobs)