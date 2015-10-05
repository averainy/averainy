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

def time_count(principle=0,interest_rate=0.08,monthly_deposit=0,target_deposit=0):
    """这个函数用来计算达到最终资产需要的月数
    参数1是初始资产，参数2是年化收益率，参数3是月递增资金，参数4是最终资产"""
    total_principle=principle
    month_count=0
    while total_principle<target_deposit:
        total_principle=total_principle*(1+interest_rate/12)+monthly_deposit
        month_count=month_count+1
    return(month_count)
def total_principle_count(principle=0,interest_rate=0.08,monthly_deposit=0,target_time=0):
    """这个函数用来计算到达指定月数之后能达到的总资产规模
    参数1是初始资产，参数2是年化收益率，参数3是月递增资金，参数4是最终月数"""
    total_principle=principle
    month_count=0
    while month_count<target_time:
        total_principle=total_principle*(1+interest_rate/12)+monthly_deposit
        month_count=month_count+1
    return(total_principle)

