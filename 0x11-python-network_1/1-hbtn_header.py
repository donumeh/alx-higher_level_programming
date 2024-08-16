#!/usr/bin/python3

"""
Makes a request to a URL and gets the header value
"""
import sys
import urllib.request


def main():
    """
    Fecthes the header data-name and value of a url
    """

    if len(sys.argv) <= 1:
        return
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers

        x_id = headers.get("X-Request-Id")

        print(x_id)


if __name__ == "__main__":
    main()
