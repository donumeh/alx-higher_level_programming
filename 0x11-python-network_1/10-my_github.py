#!/usr/bin/python3

"""
Python script that takes Github credentials username and password
and useds the api to display id
"""

import requests
import sys


def main():
    """
    Fetches the id of a github user
    """

    username = sys.argv[1]
    pat = sys.argv[2]

    url = "https://api.github.com/user"

    res = requests.get(url, auth=(username, pat))

    try:
        user_info = res.json()

        print(user_info.get("id"))

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
