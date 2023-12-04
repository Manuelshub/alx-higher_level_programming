#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            num = element
            print("{:d}".format(num), end=' ')
        print()
