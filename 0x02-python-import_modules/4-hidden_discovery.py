#!/usr/bin/python3

import hidden_4


def main():
    fns = dir(hidden_4)

    for i in fns:
        if i[0:2] == "__":
            continue
        else:
            print("{}".format(i))


if __name__ == "__main__":
    main()
