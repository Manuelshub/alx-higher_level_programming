#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    len_mat = len(matrix)
    new_matrix = [[col ** 2 for col in matrix[row]] for row in range(len_mat)]

    return new_matrix
