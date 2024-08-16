#!/usr/bin/python3

"""
Script that displays the body of the response
"""

import sys
import requests


def main():
    """
    Makes a requests and displays the body of the response
    """

    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code == 200:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")


if __name__ == "__main__":
    main()
