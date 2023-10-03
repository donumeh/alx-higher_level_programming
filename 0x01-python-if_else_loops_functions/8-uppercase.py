#!/usr/bin/python3


def uppercase(str):
    for i in str:
        case_check = ord(i)
        print(
            "{}".format(
                chr((case_check - 32))
                if case_check >= 97 and case_check <= 123
                else chr(case_check)
            ),
            end="",
        )
    print()
