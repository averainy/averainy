#!/usr/bin/python
#encoding=utf8
import re

def split(s):
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
    arraylist=re.findall(r'.{13}',s)
    if len(arraylist)*13 != len(s):
        arraylist.append(s[len(arraylist)*13:len(s)])
    return arraylist

s="123456789ab"
print split(s)
print split2(s)
