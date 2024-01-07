#!/usr/bin/python3
"""
A class with no class or attribute.
"""


class LockedClass:
    """
    This method is called when an attribute assignment is made to an instance
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            """Allow assignment for 'first_name'"""
            super().__setattr__(name, value)
        else:
            """ Raise an AttributeError for other attributes """
            message = (f"'LockedClass' object has no attribute '{name}'")
            raise AttributeError(message)
