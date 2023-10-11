#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    name = None
    value = float("-inf")

    for k, v in a_dictionary.items():
        if v > value:
            name = k
            value = v

    return name
