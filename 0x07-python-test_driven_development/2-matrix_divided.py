#!/usr/bin/python3
"""
A function that divides all the elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    new_matrix = []
    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)):
        lst = []
        for j in range(len(matrix[i])):
            if not (len(matrix[0]) == len(matrix[i])):
                msg_2 = "Each row of the matrix must have the same size"
                raise TypeError(msg_2)
            if (not isinstance(matrix[i][j], (int, float)) or
            not isinstance(matrix, list)):
                raise TypeError(msg_1)
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            elem = round(matrix[i][j] / div, 2)
            lst.append(elem)
        new_matrix.append(lst)
    return new_matrix
