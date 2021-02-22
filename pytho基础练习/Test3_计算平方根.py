""" 文档注释 """

__author__ = 'dwh'

# 创建日期 2018/12/10 13:35

import cmath

num = int(input("请输入一个数值:"))
num2 = cmath.sqrt(num)
print(type(num2))
print(num2.real)
print("%.2f 的平方根是 %.2f" % (num, num2.real))
