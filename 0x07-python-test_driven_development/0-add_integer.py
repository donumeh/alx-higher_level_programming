#!/usr/bin/python3

"""
This module contains some calculation function
Definitions:
    add_intger
"""

def add_integer(a, b=98):
    """
    This function adds two values together
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = round(a)
    if type(b) is float:
        b = round(b)

    return a + b

