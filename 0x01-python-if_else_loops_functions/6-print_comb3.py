#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print("{:d}".format(i), end='')
        print("{:d}".format(j), end='\n' if (i == 8) and (j == 9) else '')
        if (i != 8) or (j != 9):
            print(", ", end='')
