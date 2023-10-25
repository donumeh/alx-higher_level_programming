#!/usr/bin/python3


"""
This modules declares a Square class

Example:
    Square = __import__('0-square').Square

    my_square = Square()
"""


class Square:
    """
    This class creates Square objects to compute sqaures
    """
    def __init__(self, size=0):
        """
        Initialize the class with field size

        Args:
            size (type: not_known): add a new size to the square

        Returns: None
        """
        self.__size = size

    pass
