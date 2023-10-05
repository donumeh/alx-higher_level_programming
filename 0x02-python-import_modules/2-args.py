#!/usr/bin/python3

from sys import argv


def main():
    args = len(argv) - 1

    arg_type = "argument" if (args == 1) else "arguments"

    if args > 0:
        print("{:d} {}:".format(args, arg_type))

        for i in range(1, args + 1):
            print("{:d}: {}".format(i, argv[i]))
    else:
        print("{:d} {}.".format(args, arg_type))


if __name__ == "__main__":
    main()
