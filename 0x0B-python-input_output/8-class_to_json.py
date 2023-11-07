#!/usr/bin/python3

"""
Module that holds a function that returnsa dict
with simple data structure for JSON serialization
"""


def class_to_json(obj):
    """
    Function that returns a dict for JSON serialization

    Args:
        obj (obj): Class obj to return dict for

    Return: dict structure
    """

    return obj.__dict__
