#!/usr/bin/python3
"""
A function that divides all the elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    sizeof_matrix = len(matrix[0])
    new_matrix = []
    for i in range(len(matrix)):
        lst = []
        for j in range(len(matrix[i])):
            if sizeof_matrix != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            elem = round(matrix[i][j] / div, 2)
            lst.append(elem)
        new_matrix.append(lst)
    return new_matrix

