#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import time
#debug=True
debug=False

class Utility:
    def ToGB(str):
        if(debug): print(str)
        return str.decode('gb2312')

class StockInfo:
 """
 0: 未知
 1: 名字
 2: 代码
 3: 当前价格
 4: 昨收
 5: 今开
 6: 成交量（手）
 7: 外盘
 8: 内盘
 9: 买一
10: 买一量（手）
11-18: 买二 买五
19: 卖一
20: 卖一量
21-28: 卖二 卖五
29: 最近逐笔成交
30: 时间
31: 涨跌
32: 涨跌%
33: 最高
34: 最低
35: 价格/成交量（手）/成交额
36: 成交量（手）
37: 成交额（万）
38: 换手率
39: 市盈率
40: 
41: 最高
42: 最低
43: 振幅
44: 流通市值
45: 总市值
46: 市净率
47: 涨停价
48: 跌停价"""

    def GetStockStrByNum(num):
        f= urllib.request.urlopen('http://qt.gtimg.cn/q='+ str(num))
        if(debug): print(f.geturl())
        if(debug): print(f.info())
        #return like: v_s_sz000858="51~五 粮 液~000858~18.10~0.01~0.06~94583~17065~~687.07";
        return f.readline()
        f.close()

    def ParseResultStr(resultstr):
        if(debug): print(resultstr)
        slist=resultstr
        if(debug): print(slist)
        slist=slist.split('~')

        if(debug) : print(slist)

        #print('*******************************')
        print('股票名称:', slist[1])
        print('股票代码:', slist[2])

        print('当前价格:', slist[3])
        print('涨    跌:', slist[31])
        print('涨   跌%:', slist[32],'%')
        print('成交量(手):', slist[36])
        print('成交额(万):', slist[37])
        print('换手率:', slist[38],'%')
        print('市盈率:', slist[39])
        print('市净率:', slist[46])
        print('*******************************')

    def GetStockInfo(num):
        str=StockInfo.GetStockStrByNum(num)
        strGB=Utility.ToGB(str)
        StockInfo.ParseResultStr(strGB)


if __name__ == '__main__':
    stocks = ['sh600660','sh600674','sh601006','sh601166']
    for stock in stocks:
        StockInfo.GetStockInfo(stock)