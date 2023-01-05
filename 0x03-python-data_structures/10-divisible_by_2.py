#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    cp = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            cp[count] = True
        else:
            cp[count] = False
    return cp
