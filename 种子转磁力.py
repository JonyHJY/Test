#! /usr/local/bin/python
# -*- coding:gb2312 -*-
#@desc pythonͨ��BT�������ɴ�������  
#@date 2015/11/10 
#author pythontab.com 
import bencode
import sys
import hashlib
import base64
import urllib
#��ȡ���� 
torrentName = sys.argv[1] 
#��ȡ�����ļ� 
torrent = open(torrentName, 'rb').read() 
#����meta���� 
metadata = bencode.bdecode(torrent) 
hashcontents = bencode.bencode(metadata['info']) 
digest = hashlib.sha1(hashcontents).digest() 
b32hash = base64.b32encode(digest) 
#��ӡ 
print 'magnet:?xt=urn:btih:%s' % b32hash