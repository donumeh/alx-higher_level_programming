#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return result
    return result
