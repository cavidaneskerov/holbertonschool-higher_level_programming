#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new = list(map(lambda x: x * 2, row))
        new_list.append(new)
    return new_list
    return matrix
