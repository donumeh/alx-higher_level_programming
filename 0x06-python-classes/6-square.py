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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the class with field size

        Args:
            size (type: not_known): add a new size to the square

        Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        if (not isinstance(position, tuple) or len(position) != 2):
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        for i in position:
            if not isinstance(i, int):
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                        )

        self.__size = size
        self.__position = position

    def area(self):
        """
        Computes the area of a square

        Args:
            None

        Return: area of a square
        """
        return self.__size**2

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

    def my_print(self):
        """
        Prints a square

        Args:
            None

        Return:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Gets the position of the instant

        Args:
            None

        Return:
            private instance position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of an instant

        Args:
            value (int): a tuple of 2 positive integers

        Return:
            None
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        self.__position = value
