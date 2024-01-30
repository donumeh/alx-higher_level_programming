#!/usr/bin/python3
""" Module contains function that prints a square

>>> print_square(3)
###
###
###

"""

def print_square(size):
    """``print_square`` prints a square using hash (#)

    Parameters:
    size (int): the height of our square

    Return:
        void
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
    pass
