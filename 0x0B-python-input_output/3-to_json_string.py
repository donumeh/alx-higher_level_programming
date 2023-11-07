#!/usr/bin/python3

import json

"""
Module that has a function that returns
a JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """Function that returns the JSON rep to str

    Args:
        my_obj (obj): must be object that's serialization

    Return: JSON string
    """

    return json.dumps(my_obj)
