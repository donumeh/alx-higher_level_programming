#!/usr/bin/python3

"""
Module that holds a function that saves all arguments
into a Python List and saves them to a JSON file
"""


import sys
import json


def main():
    """
    Function that receives arguments and saves
    them in Python List and subsequently saves
    them in a json file

    Args: None

    Return: None
    """

    arg_list = list()
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        arg_list = load(filename)
    except Exception:
        pass

    argv_len = len(sys.argv)

    if argv_len <= 1:
        save(arg_list, filename)
    else:
        for i in range(argv_len):
            if i == 0:
                continue
            arg_list.append(sys.argv[i])
            save(arg_list, filename)
    return


if __name__ == "__main__":
    main()
