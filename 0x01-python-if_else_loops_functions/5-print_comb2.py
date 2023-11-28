#!/usr/bin/python3
for num in range(100):
    if num != 0:
        print(", ", end='')
    print("%02d" % num, end='\n' if num == 99 else '')
