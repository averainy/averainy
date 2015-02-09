#!/usr/bin/python 
#encoding=utf8
#md5_file(name)这个函数返回一个文件的md5值
import sys,os
from hashlib import md5
def md5_file(name):
	m=md5()
	fd=open(name,'rb')
	m.update(fd.read())
	fd.close()
	return m.hexdigest()
files=os.listdir('.')
for i in files:
	if os.path.isfile(i):
		print "filename:%s\t md5:%s"%(i,md5_file(i))

