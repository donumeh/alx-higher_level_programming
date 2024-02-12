import unittest
from models.base import Base

"""
This Module contains the unittest to test the class ``Base()``
found in models.base
"""


class TestBase(unittest.TestCase):

    """
    This class contains the tests for the Base class
    """

    def test_constructor_with_id(self):
        """
        Function test the base class with id passed
        """

        obj1 = Base(1)
        self.assertEqual(obj1.id, 1)

        obj2 = Base(10)
        self.assertEqual(obj2.id, 10)

    def test_constructor_without_id(self):
        """
        Function to test base without id passed
        """

        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)


if __name__ == "__main__":
    unittest.main()
