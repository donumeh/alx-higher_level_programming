#!/usr/bin/python3
import sys


def stringg(*a):
    print(*a, file=sys.stderr)
    sys.exit(1)


stringg("and that piece of art is useful - Dora Korpar, 2015-10-19")
