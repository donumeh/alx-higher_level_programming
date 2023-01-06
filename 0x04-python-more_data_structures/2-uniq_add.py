#!/usr/bin/python3


def uniq_add(my_list=[]):
    sumi = 0
    for i in set(my_list):
        sumi = i + sumi
    return sumi
