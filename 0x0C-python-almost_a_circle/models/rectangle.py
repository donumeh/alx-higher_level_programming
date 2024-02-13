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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not isinstance(id, int):
            if id is not None:
                raise TypeError("id must be an integer")

        if width <= 0:
            raise ValueError("width must be >= 0")
        if height <= 0:
            raise ValueError("height must be >= 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    def __str__(self):
        """Modified string for user"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height)

    @property
    def width(self):
        """
        Gets the width


        """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""

        if y < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):

        """displays the rectangle"""

        if self.__y:
            print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

