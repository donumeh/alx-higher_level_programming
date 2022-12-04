#!/usr/bin/python3

add = __import__("add_0").add

a = 1
b = 2

if __name__ == "__main__":
    n = add(a, b)
    print("{} + {} = {}".format(a, b, n))
