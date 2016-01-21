#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:sse.py
 
import urllib2
import urllib
import sys
import json
 
def get_value(p_dict):
    """传入一个字典来查询对应股票的市盈率
    参数结构如下:
    p_dict={
            'indexCode':index_code,
            'productId':index_code,
            'FUNDID':index_code
            }
    """
    base_url='http://query.sse.com.cn/security/fund/queryLastDayQuatByIndexAbel.do?&type=1&'
    url=base_url+urllib.urlencode(p_dict)
    print url
    req = urllib2.Request(url)
    base_refer_url='http://www.sse.com.cn/market/sseindex/indexlist/indexdetails/indexturnover/index.shtml?'
    refer_url=base_refer_url+urllib.urlencode(p_dict)
    req.add_header('Referer',refer_url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
    req.add_header('Host','query.sse.com.cn')
    r = urllib2.urlopen(req)
    receive_header = r.info()
    html = r.read()
    html = html.decode('utf-8').encode(sys.getfilesystemencoding())
    s=json.loads(html)
    print u"股票代码:%s\t市盈率:%f\t盈利收益率:%f%%"%(s['FUNDID'],s['result'][u'closeProfitRate'],1/s['result'][u'closeProfitRate']*100)
def get_data_with_id(index_code):
    """
    通过传入股票的代码来查询市盈率
    """
    p_dict={
            'indexCode':index_code,
            'productId':index_code,
            'FUNDID':index_code
            }
    get_value(p_dict)
# 
get_data_with_id('000009')
# 上证50
get_data_with_id('000016')
