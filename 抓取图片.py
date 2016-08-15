#! /usr/bin/env python 
# -*- coding=utf-8 -*-
#引入urllib库 
import urllib 
import urllib2 
import re

def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()
    page.close()  
    return html
	

'''
#写入html到文本文件
f = open('E:/url.txt','w+')
f.write(getHtml(url))
f.close()
'''
def getImg(htmlpage,n):
    reg = r'src="(url)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,htmlpage)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, 'E:/%s_%s.jpg' %(n,x))
        print '正在打印'+imgurl
        x += 1
		 
for n in range(10,16):
    url = "http://wvw.uuyishu.com:99/shenying/20101212/6476_%d.html"%n
    htmlpage = getHtml(url)
    getImg(htmlpage,n)
