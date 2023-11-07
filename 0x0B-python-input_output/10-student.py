#!/usr/bin/python3

"""
Module that contains a class Student
to store a student details
"""


class Student:
    """
    Class student that defines a student

    Public instance attr:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): the age of the student

    """

    def __init__(self, first_name, last_name, age):
        """
        Function that init the class Student
        and creates an instance of it

        Args:
            firt_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student

        Return: Create Instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function the retrieves a dictionary
        representation of a Student instance

        Args: None

        Return: dictionary representation
        """
        if attrs is None:
            return self.__dict__
        new_dict = dict()

        if isinstance(attrs, list):
            for a in attrs:
                if a in self.__dict__:
                    new_dict[a] = self.__dict__[a]
        return new_dict
