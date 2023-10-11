#!/usr/bin/python3


def weight_average(my_list=[]):
    result = 0

    if my_list is None:
        return result

    for i in my_list:
        result += i[0] * i[1]

    div = 0
    for i in my_list:
        div += i[1]

    result = result / div

    return result
