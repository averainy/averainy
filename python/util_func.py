#!/usr/bin/python
#encoding=utf8
import re
import sys
import hashlib
def replace_str(s,b):
    """
    本函数的目的是将字符串s中的"?"用列表b中的元素替换
    """
    for x in b:
        index=s.find('?')
        s=s[0:index]+x+s[index+1:]
    print s
def split(s):
    """
    按指定长度分割字符串s
    """
    arraylist=[]
    tmp=""
    num=len(s)/13+1
    yushu=len(s)%13
    if yushu==0:
        num=num-1
    for i in xrange(num):
        if i < num:
            tmp=s[i*13:i*13+13]
        else:
            tmp=s[num*13:num*13+yushu]
        arraylist.append(tmp)
    return arraylist
def splitByLen(s,lenth=1):
    """
    按指定长度len分割字符串s
    len 的默认值为1
    返回值为list
    """
    arraylist=re.findall(r'.{%d}'%lenth,s)
    if len(arraylist)*lenth != len(s):
        arraylist.append(s[len(arraylist)*lenth:len(s)])
    return arraylist
def md5(file_path):
    m2 = hashlib.md5()
    with open(file_path) as fp:
        src=fp.read(1024)
        while src:
            m2.update(src)
            src=fp.read(1024)
    return m2.hexdigest()

