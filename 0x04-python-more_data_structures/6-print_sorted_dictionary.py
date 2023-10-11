#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    dic_print(a_dictionary)


def dic_print(d):
    new_d = sorted(d)
    for i in new_d:
        print("{}: {}".format(i, d[i]))
