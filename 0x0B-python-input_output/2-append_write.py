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
    with open(filename, 'a', encoding="utf-8") as myfile:
        return myfile.write(text)
