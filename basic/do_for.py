# usr/bin/env python

# -*-encodig:utf-8-*-
for x in range(1, 10):
    for y in range(1, 10):
        if y <= x:
            print("%d * %d = %d  " % (x, y, x * y), end='')
    print()
