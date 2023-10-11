#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()

    for k, v in copy_dict.items():
        if value == v:
            del a_dictionary[k]

    return a_dictionary
