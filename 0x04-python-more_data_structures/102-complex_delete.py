#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return (a_dictionary)
    for k, v in a_dictionary.items():
        if v == value:
            del a_dictionary[k]

