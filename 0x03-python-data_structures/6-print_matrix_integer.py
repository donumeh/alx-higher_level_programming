#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
       for y in range(len(matrix[i])):
           if y == (len(matrix[i]) - 1):
               print("{:d}".format(matrix[i][y]))
           else:
               print("{:d} ".format(matrix[i][y]), end = "")
