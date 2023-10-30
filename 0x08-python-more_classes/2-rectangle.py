#!/usr/bin/python3

"""
A Module that creates a Retangle Class
"""


class Rectangle:
    """
    The class creates instances of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object
        Args:
            width (int), height (int)
        Return:
            void
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):
        """
        gets the value of the width
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        sets the value of the width
        Args:
            value (int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        gets the value of the height
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        sets the value of the height

        Args:
            value (int)
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        """
        calculates the area of the rectangle
        """

        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        """
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (2 * self._Rectangle__width) + (2 * self._Rectangle__height)
