#!/usr/bin/python3

"""Module that has a function to read file"""


def read_file(filename=""):
    """Function that reads the file"""

    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()

    print(file_content, end="")
