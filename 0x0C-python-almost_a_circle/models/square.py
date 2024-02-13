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

    def __str__(self):
        """
        Function to print out the formatted string of a class

        Parameters:
            None

        Return:
            _ (str): A formatted string
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
