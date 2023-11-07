#!/usr/bin/python3

"""
Module that write an Object to a text file
usign a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that converts an Object to a JSON file
    stored in a text file

    Args:
        my_obj (obj): Python object. Must be serializable
        filename (str): name of the file to write to

    Return: Nothing
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)

    return
