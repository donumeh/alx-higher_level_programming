#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for i, v in a_dictionary.items():
        new[i] = v * 2
    return new
