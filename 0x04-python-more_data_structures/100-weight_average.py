#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    new_list = list(map(lambda x: x[0] * x[1], my_list))
    sumi = 0
    sum_av = 0
    for i in new_list:
        sumi = sumi + i
    aver = list(map(lambda x: x[1], my_list))
    for x in aver:
        sum_av = sum_av + x
    return sumi / sum_av
