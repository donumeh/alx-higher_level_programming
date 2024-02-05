#!/usr/bin/python3

""" Module that creates an empty cclass"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """A function that raises an exception

        Parameter:
            self
        Return:
            None
        """

        raise Exception("area() is not implemented")
