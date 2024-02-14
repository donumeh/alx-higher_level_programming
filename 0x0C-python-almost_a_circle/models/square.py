#!/usr/bin/python3

"""

This module hold a class that inherits from the rectangle
module which recursively inherits from the base class

"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """
    This class creates an object square that a type
    of rectangle with all size equal

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square Class. It calls the super / base
        class to init the necessary attributes

        Parameters:
            size (int): the size of the square
            x (int): the x position to put the square
            y (int): the y position to put the square
            id (int or NoneType): the is of the obj
                    (can be found in base class)
        """

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """
        Function to print out the formatted string of a class

        Parameters:
            None

        Return:
            _ (str): A formatted string
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        """
        Getter for the square attribute size

        Parameter:
            None

        Return:
            self.__size (int)
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for the square attribute size

        Parameter:
            size (int): size of the square

        Return:
            None
        """

        self.width = size
        self.height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """
        Update - updates the attributes in the square obj

        Parameter:
            *arg (ints): a variable number of integer args
            **kwargs (ints): dictionary like argument

        Return:
            None
        """

        if args:
            attrs = ["id", "size", "x", "y"]

            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Function returns the attributes in a dictionary

        Parameters:
            None

        Return:
            attr (dict)
        """

        attr = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

        return attr
