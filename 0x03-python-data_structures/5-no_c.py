#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i in "Cc":
            continue
        else:
            new_str += i
    return new_str


if __name__ == "__main__":
    no_c(my_string)
