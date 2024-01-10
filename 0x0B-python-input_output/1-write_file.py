#!/usr/bin/python3
"""
A function that writes a string to a text file and returns the number
of characters
"""


def write_file(filename="", text=""):
    """
    Writes to a text file and returns the number of characters written.
    filename: the text file to be written to
    text: the string to be written
    """
    with open(filename, 'w') as myfile:
        myfile.write(text)
        char_num = myfile.tell()
    return char_num
