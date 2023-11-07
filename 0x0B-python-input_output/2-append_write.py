#!/usr/bin/python3

"""Module that has a function that append texts to file"""


def append_write(filename="", text=""):
    """Function that appends text to file

    Args:
        filename (str): name of the file
        text (str): text to append to file

    Return: Number of characters appended
    """

    with open(filename, "a", encoding="utf-8") as file:
        nb_chars = file.write(text)

    return nb_chars
