# usr/bin/env python

# -*-encodig:utf-8-*-

f = open('E:/pythonStudy/basic/do_try.py')
print(type(f))
print(f.name)
a = f.readlines()
print(type(a))
for  line in a:
	print(line)