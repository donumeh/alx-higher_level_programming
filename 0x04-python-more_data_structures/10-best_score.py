#!/usr/bin/python3

def best_score(a_dictionary):
    name = "None"
    if a_dictionary is None:
        return name
    num = -10000000000000
    for k, v in a_dictionary.items():
        if num < v:
            name = k
            num = v
    return name
