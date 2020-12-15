#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for i2 in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][i2]), end="")
            if i2 + 1 != len(matrix[i]):
                print(" ", end="")
        print()
