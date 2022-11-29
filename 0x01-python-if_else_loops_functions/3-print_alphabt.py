#!/usr/bin/python3

n = 26

for i in range(97, 97 + n):
    if (chr(i) == 'q') or (chr(i) == 'e'):
        continue;
    print("{}".format(chr(i)), end="")
