#!/usr/bin/python3
"""
A class that inherits
"""


class MyList(list):
    """
    A class that inherits and adds a method to print in sorted order
    """
    def print_sorted(self):
        """
        Prints in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
