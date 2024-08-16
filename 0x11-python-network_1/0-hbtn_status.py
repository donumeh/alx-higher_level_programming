#!/usr/bin/python3

"""
Fecthes http using urllib
"""
import urllib.request


def main():
    """
    Fecthes url using urllib
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == "__main__":
    main()
