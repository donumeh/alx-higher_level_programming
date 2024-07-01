#!/usr/bin/python3

"""
A script that lists all states from the database
"""

import MySQLdb
import sys


def main():
    """
    Connect to mysql database using passed args
    """
    interface = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3],
    )

    session = interface.cursor()

    # query table for states
    session.execute("SELECT * FROM states ORDER BY states.id")
    result = session.fetchall()

    # print result
    for r in result:
        print(r)

    # close sesssion and interface
    session.close()
    interface.close()


if __name__ == "__main__":
    main()
