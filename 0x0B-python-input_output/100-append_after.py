#!/usr/bin/python3
""" Function that inserts a line of text to a file, after each line
containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file.
    filename: the name of the file.
    search_string: the specific string to be searched for.
    new_string: the new string to be appended after that string
    """
    new_line = ""
    with open(filename, 'r') as myfile:
        for line in myfile:
            new_line += line
            if search_string in line:
                new_line += new_string
    with open(filename, 'w') as newfile:
        newfile.write(new_line)
