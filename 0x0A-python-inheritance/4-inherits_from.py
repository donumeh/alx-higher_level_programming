#!/usr/bin/python3

"""Module holds a function that checks if an object is a subclass
of a class
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class


    Paramter:
        obj (obj): the value to check
        a_class (class): the class name to check on

    Return:
        True if the object is an instance of class
        that inherited directly or indirectly, otherwise false
    """
    class_name = type(obj)
    return issubclass(class_name, a_class) and class_name != a_class
