#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) > 1:
        if (len(argv) - 1) == 1:
            print("{:d} argument:".format(len(argv) - 1))
        elif (len(argv) - 1) > 1:
            print("{:d} arguments:".format(len(argv) - 1))
        n = 0
        for i in argv[1:]:
            n = n + 1
            print("{:d}: {:s}".format(n, i))
