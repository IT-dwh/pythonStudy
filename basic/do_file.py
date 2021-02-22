f = open('./do_try.py')
print(type(f))
print(f.name)
a = f.readlines()
print(type(a))
for line in a:
    print(line)
