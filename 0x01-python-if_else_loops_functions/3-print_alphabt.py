#!/usr/bin/python3

q = ord("q")
e = ord("e")

for i in range(97, 123):
    if i != q and i != e:
        print("{}".format(chr(i)), end="")
