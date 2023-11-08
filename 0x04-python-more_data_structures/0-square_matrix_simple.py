#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = list()
    items = list()

    for i in matrix:
        for j in i:
            items.append(j ** 2)
        new.append(items)
        items = []

    return new
