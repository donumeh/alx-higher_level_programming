#!/usr/bin/python3

"""
divide a matrix with a div number
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix with an int

    Args:
        matrix (nested list): the list to divide
        div (int) the value to divide with

    Raises:
        TypeError: if not list of lists, div is NaN, and rows != same size
        ZeroDivisionError: if div is 0

    Return: a new matrix
    """
    err_typ1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_typ2 = "Each row of the matrix must have the same size"
    err_typ3 = "div must be a number"
    err_zero_div = "division by zero"
    size_index = 0

    if type(matrix) is list:
        if len(matrix) == 0:
            raise TypeError(err_typ1)
        else:
            for i in matrix:
                if type(i) is not list:
                    raise TypeError(err_typ1)
                else:
                    if size_index == 0:
                        size_index = len(i)
                    else:
                        if size_index != len(i):
                            raise TypeError(err_typ2)
    else:
        raise TypeError(err_typ1)

    if div == 0:
        raise ZeroDivisionError(err_zero_div)
    if type(div) not in [int, float]:
        raise TypeError(err_typ3)

    new_matrix = []
    for rows in matrix:
        new_row = []
        for num in rows:
            if type(num) not in [int, float]:
                raise TypeError(err_typ1)
            else:
                new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
