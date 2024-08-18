#!/usr/bin/python3

"""
Gets the last committers of a repository
"""

import sys
import requests


def main():
    """
    Gets the last committers of a repos
    """

    repos = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repos}/commits"

    headers = {"accept": "application/vnd.github+json"}

    res = requests.get(url, headers=headers)
    commits = res.json()

    for commit in commits[:10]:
        commit_hash = commit.get("sha")
        commit_user = commit.get("commit").get("author").get("name")

        print(f"{commit_hash}: {commit_user}")


if __name__ == "__main__":
    main()
