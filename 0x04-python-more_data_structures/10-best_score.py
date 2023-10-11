#!/usr/bin/python3


def best_score(a_dictionary):
    name = ""
    value = 0

    if a_dictionary is None:
        return None

    for k, v in a_dictionary.items():
        if v > value:
            name = k
            value = v

    return name
