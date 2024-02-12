#!/usr/bin/python3

"""
This Module contains the base class of all other classes in this project

"""


class Base:

    """
    This Class is the base of all other classes in this project.

    The goal of it is to manage `id` attribute in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function contains the initialization of the Base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
