#!/usr/bin/python3

"""
This Module tests the class Sqaure which is an inheritance of
Retangle, and itself an inheritance of Base class
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    """
    This class is derived from the unittest TestCase and it
    tests if the constructor and inherited attributes and behaviours
    works perfectly well
    """

    def test_constructor(self):
        """
        This function tests the constructor of the Square() object

        Parameters:
            None

        Return:
            None
        """

        square = Square(5, 1, 2, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_setters_and_getters(self):
        """
        This function tests the setters and getters inherited from its
        parent to know if it works in the derived class without any issue

        Parameter:
            None

        Return:
            None
        """

        square = Square(5, 1, 2, 10)

        with self.assertRaises(TypeError):
            square.width = "invalid"

        with self.assertRaises(ValueError):
            square.width = 0

        with self.assertRaises(TypeError):
            square.x = "invalid"

        with self.assertRaises(ValueError):
            square.x = -5

        with self.assertRaises(TypeError):
            square.y = "invalid"

        with self.assertRaises(ValueError):
            square.y = -5

        with self.assertRaises(TypeError):
            square.size = "invalid"

        with self.assertRaises(ValueError):
            square.size = 0

    def test_str(self):
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")


if __name__ == "__main__":
    unittest.main()
