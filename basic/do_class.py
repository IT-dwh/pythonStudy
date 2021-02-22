class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def run():
        print("run")

    def eat(self, food):
        print("%s eat %s" % (self.name, food))


p = Person("dwh", 20)
p.run()
p.eat("apple")

p2 = Person("汤姆", 30)
p2.run()
p2.eat("banana")
