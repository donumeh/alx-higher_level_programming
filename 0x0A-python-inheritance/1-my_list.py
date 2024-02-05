#!/usr/bin/python3

"""This module contains a class that inherits from List"""


class MyList(list):

    """This program inherits from list and builds ontop of it"""

    def print_sorted(self):
        """Sorted the lists and prints

        Parameter:
            none

        Return:
            none
        """

        sorted_list = sorted(self, reverse=False)
        print(sorted_list)
