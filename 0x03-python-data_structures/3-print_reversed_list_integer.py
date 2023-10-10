#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    new_list = sorted(my_list, reverse=True)
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))


if __name__ == "__main__":
    print_reversed_list_integer(my_list)
