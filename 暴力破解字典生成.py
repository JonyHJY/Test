#!usr/bin/env python
#-*-coding:utf-8-*-
import itertools as its
words = "ABCDEFGHIJKLMNOPQRS"
r = its.product(words,repeat=6)
dic = open("pass.txt","a")
for i in r:
    dic.write(" ".join(i))
	
dic.close()
