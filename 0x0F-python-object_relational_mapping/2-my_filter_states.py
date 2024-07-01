#!/usr/bin/python3

"""
A script that takes in an argument and displays all values
"""

import MySQLdb
import sys


def main():
    """
    Connects to a database and accesses data from a table
    """

    interface = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )
    state_name = sys.argv[4] if sys.argv[4] is not None else None

    # create a session

    session = interface.cursor()

    session.execute(
        "SELECT * FROM states \
                WHERE BINARY states.name = '{}' \
                ORDER BY states.id".format(
            state_name
        )
    )

    result = session.fetchall()

    for r in result:
        print(r)

    session.close()
    interface.close()


if __name__ == "__main__":
    main()
