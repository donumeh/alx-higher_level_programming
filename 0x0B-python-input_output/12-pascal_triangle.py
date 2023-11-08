#!/usr/bin/python3

"""
Module holds a function that returns
pascal's triangle
"""


def pascal_triangle(n):
    """
    Function that represents the pascal triangle
    and returns in a compound list

    Args:
        n (int): number of rows of triangle

    Return: compound list
    """

    cmp_list = []

    if n <= 0:
        return cmp_list

    for i in range(n):
        nest_list = []

        if i == 0:
            nest_list.append(1)
            cmp_list.extend([nest_list])
            continue
        a = 0
        b = 0
        value = 0

        for num in range(len(cmp_list[i - 1])):
            b = cmp_list[i - 1][num]
            value = a + b

            nest_list.append(value)
            a = b

            if (num + 1) == len(cmp_list):
                b = 0

        value = a + b
        nest_list.append(value)
        cmp_list.extend([nest_list])
    return cmp_list
