#!/usr/bin/python3

from models.base import Base

"""
Modules has a class that inherits from Base
"""


class Rectangle(Base):

    """
    This Class creates a rectangle object using the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Function initiates the class module Rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        self.__width = width

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height"""
        self.__height = height

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x"""
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""
        self.__y = y
