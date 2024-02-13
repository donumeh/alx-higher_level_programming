#!/usr/bin/python3

"""
Modules has a class that inherits from Base

The Rectangle class is a shape constructing object used
in creating and replicating the shape behaviours

It can:
    calculate the area
    print the shape out
    and add some graph spacing to it
"""
from models.base import Base

class Rectangle(Base):

    """
    This Class creates a rectangle object using the base class

    Methods/Behaviours:
        __init__ : constructor
        __str__ : string formater
        width, height, x, y : setters and getters
        area: displays the area of the rectangle
        display: displays the rectangle by printing it to screen
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Function initiates the class module Rectangle

        Parameters:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x graph position of the rectangle
            y (int): the y position of the rectangle
            id (int or NoneType): the id of the rectangle, passed to base class

        Return:
            None

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
        """Modified string for user

        Reformats the print out of the rectangle object

        Parameters:
            None

        Return:
            None
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height)


    @property
    def width(self):
        """
        Getter of the width attribute

        Parameters:
            None

        Return:
            self.__width (int)

        """
        return self.__width


    @width.setter
    def width(self, width):
        """Sets the width

        Setter of the width attribute

        Parameters:
            width (int): the new width of the rectangle object

        Return:
            None
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width


    @property
    def height(self):
        """Gets the height

        Getter of the height attribute

        Parameters:
            None

        Return:
            None
        """

        return self.__height


    @height.setter
    def height(self, height):
        """Sets the height

        Setter of the height attribute in the rectangle obj

        Parameter:
            height (int): the new height of the obj

        Return:
            None
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height


    @property
    def x(self):
        """Gets x

        Getter of the x attribute in the rect obj positioning

        Parameter:
            None

        Return:
            self.__x (int): the x value of the rect obj
        """

        return self.__x


    @x.setter
    def x(self, x):
        """Sets x

        Setter of the x attribute in the rrect obj positioning

        Parameter:
            x (int): the new value of the x attribute

        Return:
            None
        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x


    @property
    def y(self):
        """Get y

        Getter of the y attribute in the rectangle obj positioning


        Parameter:
            None

        Return:
            self.__y (int): the value of y attribute in rect
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Set y

        Setter of the y attribute in the rectangle obj positioning

        Parameter:
            y (int): the new value of the attribute

        Return:
            None
        """

        if y < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        self.__y = y

    def area(self):
        """returns the area of the rectangle

        Area - finds the area of the rectangle object

        Parameter:
            None

        Return:
            height * width (attrs)
        """
        return self.__height * self.__width

    def display(self):

        """displays the rectangle

        Display - displays the rectangle by printing it unto the screen using '#'

        Parameter:
            None

        Return:
            None

        """

        if self.__y:
            print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

