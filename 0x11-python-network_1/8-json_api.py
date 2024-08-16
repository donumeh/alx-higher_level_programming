#!/usr/bin/python3

"""
Sends a POST req to rul
"""

import requests
import sys


def main():
    """
    Takes a letter and sends a POST req
    """

    if len(sys.argv) < 2:
        param = ""
    else:
        param = sys.argv[1]

    data = {"q": param}

    res = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_dict = res.json()

        if len(json_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_dict["id"], json_dict["name"]))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
