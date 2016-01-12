#!/usr/bin/python
#coding=utf8
"""
# Author: yxzhang
# Created Time : Tue 12 Jan 2016 11:28:50 AM JST

# File Name: etf_test.py
# Description:

"""
import random

all_shares=0
start_price=1
fee_rate=0.001
auto_pay=10
all_pay=0
aver_price=0
shouyilv=0
all_shouyi=0
zongchengben=0
def growth_rates():
    """
    涨跌幅
    """
    return random.uniform(-0.04, 0.04)
def get_shares():
    all_shares=all_shares+(auto_pay*(1-fee_rate))/start_price

def abc(shijian):
    global start_price
    global all_shares
    global all_pay
    global shouyilv
    global all_shouyi
    global zongchengben
    for i in xrange(0,shijian):
        growth=growth_rates()
        start_price=start_price*(1+growth)
        if all_pay!=0:
            shouyilv=(all_shares*start_price-all_pay)/all_pay
        if all_shares!=0 and shouyilv>=0.1 and start_price>2:
            all_shouyi=all_shouyi+all_shares*start_price-all_pay
            zongchengben=zongchengben+all_pay
            all_shares=0
            all_pay=0
            shouyilv=0
            continue
        if start_price>1:
            continue
        if growth>=0:
            continue
        all_shares=all_shares+(auto_pay*(1-fee_rate))/start_price
        all_pay=all_pay+auto_pay
    #print u"总成本：%f"%(all_pay)
    #print u"总份额：%f"%(all_shares)
    #print u"当前净值：%f"%(start_price)
    #if all_shares==0:
        #print u"平均成本：0"
    #else:
        #print u"平均成本：%f"%(all_pay/all_shares)
    #if all_pay==0:
        #print u"收益率: 0"
    #else:
        #print u"收益率: %f"%((all_shares*start_price-all_pay)/all_pay)
    all_shouyi=all_shouyi+all_shares*start_price-all_pay
    print "每天收益: %f"%(all_shouyi/shijian)
    print "收益: %f"%(all_shouyi)
    zongchengben=zongchengben+all_pay
    print "总成本: %f"%(zongchengben)


abc(3650)
