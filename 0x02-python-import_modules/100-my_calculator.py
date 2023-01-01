#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    if arg_num() == 1:
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} + {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} + {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)


def arg_num():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
