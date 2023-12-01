#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1
if num_args == 0:
    print(num_args)
else:
    total_sum = 0
    for i in range(num_args):
        args = int(sys.argv[i + 1])
        total_sum += args
    print(total_sum)
