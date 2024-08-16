#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a req to the url and displays the body
"""

import sys
import urllib.request


def main():
    """
    Request for url and handle HTTPError
    """

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)

    except urllib.error.HTTPError as http_err:
        print(f"Error code: {http_err.code}")


if __name__ == "__main__":
    main()
