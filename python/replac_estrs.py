#!/usr/bin/python
import sys,os
import commands
def delstrs(file):
	"""这里实现的是替换file中出现的ppstr字符串，这里没用正则表达式，只是使用了字符串处理函数replace"""
	ppstr='<script type="text/javascript">/*120*270\xef\xbc\x8c\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\x8e2012-9-6\xef\xbc\x8c\xe4\xbd\x8d\xe4\xba\x8ec4xxxx.xxxxxxx.xxx*/ var cpro_id = \'u1051122\';</script><script src="http://cpro.baidustatic.com/cpro/ui/f.js" type="text/javascript"></script>'
	f=open(file)
	strs=f.read()
	strs=strs.replace(ppstr,'')
	f.close()
	f=open(file,'w')
	f.write(strs)
	f.close()
for file in commands.getoutput('ls %s'%sys.argv[1]).split('\n'):
	"""commands这个库很实用，"""
	filename='/'.join((sys.argv[1],file))
	if os.path.isfile(filename):
		print filename
		delstrs(filename)
