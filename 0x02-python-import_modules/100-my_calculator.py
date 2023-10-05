#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    args = len(argv) - 1
    if args != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = ["+", "-", "*", "/"]
    result = 0
    op_check = True if (argv[2] in operators) else False

    if not op_check:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    fns = [add, sub, mul, div]

    index = 0
    for operator in operators:
        if operator == argv[2]:
            result = fns[index](a, b)
            pass
        else:
            index = index + 1
            continue

    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, result))


if __name__ == "__main__":
    main()
