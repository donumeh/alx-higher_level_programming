#!/usr/bin/python3

for i in range(0, 90):
    unit = i % 10
    tens = i / 10

    if tens > unit or tens == unit:
        continue
    if i != 89:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
