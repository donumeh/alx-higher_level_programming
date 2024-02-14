#!/usr/bin/python3

"""
This Module contains the base class of all other classes in this project

"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that returns a JSON string representation of a dict

        Paramters:
            list_dictionaries (dict): dict to representation

        Return:
            None
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function saves a JSOn string rep into a file

        Parameters:
            list_objs (list): list of dict object

        Return:
            None
        """

        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(cls.to_json_string(None))
        else:
            list_dict = []

            for i in list_objs:
                list_dict.append(i.to_dictionary())

            with open(filename, "w", encoding="utf-8") as file:
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Function that returns the list of the JSON string representation

        Parameter:
            json_string (string): a json string format

        Return:
            python obj (list) of dict
        """

        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Function returns an instance with all attributes already set

        Parameter:
            dictionary (dict): a dictionary of obj attribute data

        Return:
            obj
        """

        if cls.__name__.lower() == "rectangle":
            instance = cls(1, 1)
        elif cls.__name__.lower() == "square":
            instance = cls(1)

        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """
        Function will load json from file

        Parameter:
            None

        Return:
            obj instance
        """

        list_instances = []

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                file_content = file.read()

            if file_content:
                list_dict = Base.from_json_string(file_content)

                for i in list_dict:
                    instance = cls.create(**i)
                    list_instances.append(instance)

        except FileNotFoundError:
            pass

        return list_instances
