#!/usr/bin/python3

"""
This Module contains the file that tests the rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """
    Class with super class TestCase to test the rectangle base
    """

    def test_constructor(self):
        """
        Method to test the constructor of the rectangle class
        """

        rect = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_setters_and_getter(self):
        """
        Method to test the setters and getter of constructor
        """

        rect = Rectangle(10, 20, 5, 5, 1)
        rect.width = 15
        rect.height = 25
        rect.x = 10
        rect.y = 10

        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 10)

    def test_raises(self):
        """Tests for error raised"""

        rect = Rectangle(10, 20, 5, 5)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = 0

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -5

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5


if __name__ == "__main__":
    unittest.main()
