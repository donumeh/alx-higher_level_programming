#!/usr/bin/python3

"""
Module that has a function tha converts
from JSON Object (string) to Python Object
"""


import json


def from_json_string(my_str):
    """
    Function that converts a JSON object (string)
    into a Python Object

    Args:
        my_str (str): the formatted JSON string

    Return: returns a Python Object
    """

    py_obj = json.loads(my_str)
    return py_obj
