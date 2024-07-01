#!/usr/bin/python3

"""
A script that lists all `states` with a name tarting with N (upper case)
"""

import MySQLdb
import sys


def main():
    """
    Connect to the database and print result
    """
    interface = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host="localhost",
    )

    session = interface.cursor()

    session.execute(
        "SELECT * FROM states WHERE name lIKE 'N%' \
                    ORDER BY states.id"
    )
    result = session.fetchall()

    for r in result:
        print(r)

    session.close()
    interface.close()


if __name__ == "__main__":
    main()
