#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c += 1
            if c == len(matrix[0]):
                print("{:d}".format(matrix[i][j]), end='')
                c = 0
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
        print()
