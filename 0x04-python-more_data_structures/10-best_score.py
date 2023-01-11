#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    num = -10000000000000
    name = ''
    for k, v in a_dictionary.items():
        if num < v:
            name = k
            num = v
    return name
