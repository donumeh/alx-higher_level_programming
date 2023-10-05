#!/usr/bin/python3

from sys import argv


def main():
    sum_of_args = 0

    num_of_args = len(argv)

    for i in range(1, num_of_args):
        sum_of_args = sum_of_args + int(argv[i])
    print(sum_of_args)


if __name__ == "__main__":
    main()
