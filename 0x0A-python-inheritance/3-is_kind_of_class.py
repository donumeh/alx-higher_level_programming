#!/usr/bin/python3

"""Module holds a function that check if class is an instance
off an object
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of class

    Parameter:
        obj (obj): the value of a class object
        a_class: the name of class obj

    Return:
        True if obj is exactly of type a_class
        Otherwise False
    """
    return isinstance(obj, a_class)
