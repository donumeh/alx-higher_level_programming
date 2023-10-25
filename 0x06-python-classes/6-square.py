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

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple):
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        if len(position) != 2:
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        for i in position:
            if i < 0 or not isinstance(position, tuple):
                raise TypeError(
                        "position must be a tuple of 2 positive integrs"
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
        num = self.__size
        if num != 0:
            i = 0
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            while i < num:
                print(" " * self.__position[0], end="")
                print("#" * num)
                i += 1
        else:
            print()

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
        if not isinstance(value, tuple):
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        if len(value) != 2:
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        for i in value:
            if i < 0 or not isinstance(value, tuple):
                raise TypeError(
                        "position must be a tuple of 2 positive integrs"
                        )
        self.__position = value
