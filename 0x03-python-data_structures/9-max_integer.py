#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == "":
        return None
    max_val = 0
    for i in range(len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]
        else:
            continue

    return max_val
