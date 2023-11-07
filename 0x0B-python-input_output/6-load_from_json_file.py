#!/usr/bin/python3

"""
Module that holds a function that loads
from a json file and converts into Python Obj
"""


import json


def load_from_json_file(filename):
    """
    Function that converts json file into
    Python Object

    Args:
        filename (str): name of file that contains the json file

    Return: Python obj
    """

    with open(filename, "r") as file:
        data = json.load(file)

    return data
