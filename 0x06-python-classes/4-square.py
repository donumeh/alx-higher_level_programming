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

        Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of a square

        Args:
            None

        Return: area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the value of size

        Return: value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size

        Args:
            value (int): param of type int to set instance attr size

        Return: void
        """

        # raise TypeError if value isn't int
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # raise ValueError if value appears to be negative
        if value < 0:
            raise ValueError("size must be >= 0")
        # else set size
        self.__size = value
