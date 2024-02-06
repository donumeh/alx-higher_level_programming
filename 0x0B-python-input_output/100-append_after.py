#!/usr/bin/python3

"""This moduel contains a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in file_content:
            if search_string in line:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
