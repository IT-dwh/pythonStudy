#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''连接数据库练习'''

import sys
import datetime
import openpyxl
__auther__ = '杜文豪'


def getData(startDate, endDate):
    path = 'C:/Users/admin/Desktop/需求/李冬冬/搜索sugg数据/test.xlsx'
    wb = openpyxl.load_workbook(path)
    getData_pvuv(wb)
    getData_order(wb)
    wb.save(path)


if __name__ == '__main__':
    targetDate = datetime.datetime.today()  # 默认是今日
    if len(sys.argv) > 1:
        # 有指定日期
        targetDate = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')

    # 执行查询的开始和结束日期
    startDate = targetDate - datetime.timedelta(days=7)
    endDate = targetDate - datetime.timedelta(days=1)

    getData(startDate, endDate)
