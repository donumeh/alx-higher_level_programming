#!/usr/bin/python3

"""
This module contains some calculation function
Definitions:
    add_intger
"""


def add_integer(a, b=98):
    """
    This function adds two values together

    Args:
        a: first int.
        b: second int, default value is 98

    Raises:
        TypeError: if a, b are neither int nor float

    Returns:
        sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(round(a)) + int(round(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
