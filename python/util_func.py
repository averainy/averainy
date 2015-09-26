#!/usr/bin/python
#encoding=utf8
import re
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
def split2(s):
    """
    按指定长度分割字符串s
    """
    arraylist=re.findall(r'.{13}',s)
    if len(arraylist)*13 != len(s):
        arraylist.append(s[len(arraylist)*13:len(s)])
    return arraylist

