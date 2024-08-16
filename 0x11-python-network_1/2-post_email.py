#!/usr/bin/python3

"""
Python script that takes in a url and an email and send a post req
"""

import sys
import urllib.request
import urllib.parse


def main():
    """
    Sends a post req to a server
    """

    if len(sys.argv) < 3:
        return

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    data_encode = urllib.parse.urlencode(data)
    data_encode = data_encode.encode("ascii")
    req = urllib.request.Request(url, data_encode)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
