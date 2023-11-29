#!/usr/bin/python3

def remove_char_at(str, n):
    s = str[:n]
    t = str[n + 1:]
    return (s + t)
