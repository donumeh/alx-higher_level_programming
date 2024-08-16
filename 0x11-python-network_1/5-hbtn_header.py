#!/usr/bin/python3

"""
Python script that takes in a URL
send a req and displays the value
"""

import requests
import sys


def main():
    """
    Fecthes a url using request lib
    """

    url = sys.argv[1]

    res = requests.get(url)
    headers = res.headers

    print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
