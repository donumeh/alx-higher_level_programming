#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for i, v in a_dictionary.items():
        if i == key:
           del a_dictionary[key]
           break
    return (a_dictionary)
