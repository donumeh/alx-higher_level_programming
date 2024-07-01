#!/usr/bin/python3

"""
A script that lists all cities from the database
"""

import MySQLdb
import sys


def main():
    """
    Connects to mysql and prints out values
    """

    interf = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )
    ses = interf.cursor()

    ses.execute(
        "\
            SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON states.id = cities.state_id"
    )
    result = ses.fetchall()

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
