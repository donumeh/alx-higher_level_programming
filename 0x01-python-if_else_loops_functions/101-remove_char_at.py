#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = ""

    if (len(str) < n) or (n < 0):
        return str

    for i in str:
        if str[n] == i:
            continue
        else:
            new_str += i
    return new_str
