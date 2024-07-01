#!/usr/bin/python3

"""
A script that takes in name of state as an arg and list all
"""

import MySQLdb
import sys


def main():
    """
    Connects to a database and print out the values
    """

    interf = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )
    city_name = sys.argv[4]

    ses = interf.cursor()

    ses.execute(
        "SELECT cities.name FROM cities \
                    JOIN states ON states.id = cities.state_id \
                    WHERE states.name = %s",
        ((city_name,)),
    )
    result = ses.fetchall()

    res = []

    for r in result:
        res.append(r[0])

    print(", ".join(res))


if __name__ == "__main__":
    main()
