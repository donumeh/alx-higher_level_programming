#!/usr/bin/python3

"""Module that has a function that writes to a file"""


def write_file(filename="", text=""):
    """Function that writes to a file"""

    with open(filename, "w", encoding="utf-8") as file:
        nb_chars = file.write(text)

    return nb_chars
