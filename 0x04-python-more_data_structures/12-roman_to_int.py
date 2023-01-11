#!/usr/bin/python3

def check_roman(x):
    if x == "I":
        return 1
    if x == "IV":
        return 4
    if x == "V":
        return 5
    if x == "IX":
        return 9
    if x == "X":
        return 10
    if x == "XL":
        return 40
    if x == "L":
        return 50
    if x == "XC":
        return 90
    if x == "C":
        return 100
    if x == "CD":
        return 400
    if x == "D":
        return 500
    if x == "CM":
        return 900
    if x == "M":
        return 1000


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    sumi = 0
    for i in range(len(roman_string)):
        if (roman_string[i] == "I") and (i != (len(roman_string) - 1)):
            if roman_string[i + 1] == "V":
                i = i + 1
                sumi = sumi + check_roman("IV")
            elif roman_string[i + 1] == "X":
                i = i + 1
                sumi = sumi + check_roman("IX")
            else:
                sumi = sumi + check_roman(roman_string[i])
        elif roman_string[i] == "X" and (i != (len(roman_string) - 1)):
            if roman_string[i + 1] == "L":
                i = i + 1
                sumi = sumi + check_roman("XL")
            elif roman_string[i + 1] == "C":
                i = i + 1
                sumi = sumi + check_roman("XC")
            else:
                sumi = sumi + check_roman(roman_string[i])
        elif roman_string[i] == "C" and (i != (len(roman_string) - 1)):
            if roman_string[i + 1] == "D":
                i = i + 1
                sumi = sumi + check_roman("CD")
            elif roman_string[i + 1] == "M":
                i = i + 1
                sumi = sumi + check_roman("CM")
            else:
                sumi = sumi + check_roman(roman_string[i])
        else:
            sumi = sumi + check_roman(roman_string[i])
    return sumi
