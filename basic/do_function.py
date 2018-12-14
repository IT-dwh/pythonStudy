# usr/bin/env python

# -*-encodig:utf-8-*-

from collections import Iterable


l = [x + x for x in range(1, 100)]
g = (x + x for x in range(1, 100))
print(type(l))  # 列表生成式：直接方式生成列表
print(type(g))  # 迭代器：next一次，计算一次值
