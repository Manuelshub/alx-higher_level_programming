#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing
the pascals triangle.
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascals
    triangle.
    n: the size of the list of lists
    """
    if n <= 0:
        return []
    else:
        result = [[1]]

        for i in range(n - 1):
            tmp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) +  1):
                row.append(tmp[j] + tmp[j + 1])
            result.append(row)
        return result
