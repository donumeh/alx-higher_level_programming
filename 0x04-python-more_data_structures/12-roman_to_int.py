#!/usr/bin/python3


def roman_to_int(roman_string):
    numerals = \
            {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = ""
    current = ""
    for char in roman_string:
        for key, value in numerals.items():
            current = char

            if current == "X":
                if prev == "I":
                    result -= 2
            elif current == "L":
                if prev == "X":
                    result -= 20
            elif current == "C":
                if prev == "X":
                    result -= 20
            elif current == "D":
                if prev == "C":
                    result -= 200
            elif current == "M":
                if prev == "C":
                    result -= 200
            prev = char
            if char == key:
                result += value
    return result
