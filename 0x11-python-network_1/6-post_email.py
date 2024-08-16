#!/usr/bin/python3

"""
Python script that takes in a URL and an email addr
sends a POST req to the url and displays a body
"""

import sys
import requests


def main():
    """
    Fetches the url and sends a post data
    """

    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    res = requests.post(url, data=data)

    print(res.text)


if __name__ == "__main__":
    main()
