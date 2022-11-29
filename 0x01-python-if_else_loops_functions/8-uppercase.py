#!/usr/bin/env python3


def uppercase(str):
    for i in str:
        if (i >= "a") and (i <= "z"):
            c = ord(i) - 32
        else:
            c = ord(i)
        print("{}".format(chr(c)), end="")
    print()
