""" 文档注释 """

__author__ = 'dwh'

# 创建日期 2018/12/14 17:16
a = float(input("输入三角形第一边长:"))
b = float(input("输入三角形第二边长:"))
c = float(input("输入三角形第三边长:"))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("area: %0.2f" % area)
