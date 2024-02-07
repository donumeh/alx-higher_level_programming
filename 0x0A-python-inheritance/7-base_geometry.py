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

    def integer_validator(self, name, value):
        """Module that validates a value

        Paramter:
            name (str): string or key
            value (int): the integer to validate

        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
