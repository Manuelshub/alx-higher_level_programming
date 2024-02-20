#!/usr/bin/python3
"""
A function that prints a text with 2 new lines after each of these
characters: ., ?, :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after some characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    for i in range(len(text)):
        if text[i - 1] in characters and text[i] == ' ':
            continue
        print(text[i], end='')
        if text[i] in characters:
            print()
            print()
