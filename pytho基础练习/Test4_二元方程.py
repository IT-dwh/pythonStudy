""" 文档注释 """

__author__ = 'dwh'

# 创建日期 2018/12/14 16:22

import cmath

a = float(input("输入a:"))
b = float(input("输入b:"))
c = float(input("输入c:"))

d = (b**2) - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("结果为: %.2f 和 %.2f" % (sol1.real, sol2.real))
