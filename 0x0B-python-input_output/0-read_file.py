#!/usr/bin/python3
"""
This function reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a file and prints it out.
    filename: the file to be read.
    """
    with open(filename, 'r', encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end='')
