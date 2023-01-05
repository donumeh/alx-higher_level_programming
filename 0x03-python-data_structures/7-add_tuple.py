#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    first1 = 0
    first2 = 0
    second1 = 0
    second2 = 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            first1 = tuple_a[0]
    elif len(tuple_a) >= 2:
        first1 = tuple_a[0]
        first2 = tuple_a[1]

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            second1 = tuple_b[0]
    elif len(tuple_b) >= 2:
        second1 = tuple_b[0]
        second2 = tuple_b[1]

    sum1 = first1 + second1
    sum2 = first2 + second2
    tp = sum1, sum2
    return tp
