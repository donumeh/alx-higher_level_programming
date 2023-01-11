#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    count = 0;
    for i, v in a_dictionary.items():
        count = count + 1
        if i == key:
            a_dictionary[i] = value
        elif (i != key) and (count == len(a_dictionary)):
            a_dictionary[key] = value
            break
    return a_dictionary    
