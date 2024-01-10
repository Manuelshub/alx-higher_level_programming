#!/usr/bin/python3
"""
This Function appends a string at the end of a text file and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.
    filename: the file to be appended to.
    text: the strig to be appended.
    """
    with open(filename, 'a') as myfile:
        myfile.write(text)
        char_num = myfile.tell()
    return char_num
