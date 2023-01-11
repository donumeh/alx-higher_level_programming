#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) != str:
        return 0
    stri = roman_string
    r = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and r[stri[i]] > r[stri[i - 1]]:
            result += r[stri[i]] - 2 * r[stri[i - 1]]
        else:
            result += r[stri[i]]
    return result
