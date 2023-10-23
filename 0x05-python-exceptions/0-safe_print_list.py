#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    int i = 0;
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError as e:
            pass
    return i

