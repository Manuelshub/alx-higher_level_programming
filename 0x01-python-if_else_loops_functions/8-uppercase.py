#!/usr/bin/python3

def uppercase_letter(c):
    if (ord(c) >= 97) and (ord(c) <= 122):
        return ord(c) - 32
    else:
        return ord(c)

def uppercase(str):
    strings = ""
    for ch in str:
        strings += "%c" % uppercase_letter(ch)
    print("{:s}".format(strings))
