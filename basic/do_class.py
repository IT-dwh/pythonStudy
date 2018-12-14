#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def run(self):
		print("run")
	def eat(self, food):
		print("%s eat %s" % (self.name, food))

p = Person("dwh",20)
p.run()
p.eat("apple")

p2 = Person("dwj",30)
p2.run()
p2.eat("banana")