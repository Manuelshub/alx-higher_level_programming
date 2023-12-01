#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print(num_args, "arguments.")
    else:
        if num_args == 1:
            print(num_args, "argument:")
        else:
            print(num_args, "arguments:")
        for i in range(num_args):
            args = sys.argv[i + 1]
            print("{}:".format(i + 1), args)
