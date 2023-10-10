#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div_check = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_check.append(True)
        else:
            div_check.append(False)

    return div_check


if __name__ == "__main__":
    divisible_by_2(my_list)
