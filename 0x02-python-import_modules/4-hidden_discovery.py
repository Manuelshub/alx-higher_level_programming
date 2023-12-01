#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    num_args = len(dir(hidden_4))
    for i in range(num_args):
        if not dir(hidden_4)[i].startswith("__"):
            print(dir(hidden_4)[i])
