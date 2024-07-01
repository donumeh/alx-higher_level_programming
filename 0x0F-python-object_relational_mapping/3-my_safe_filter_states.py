#!/usr/bin/python3

"""
A script that takes in argument in safe mode
"""

import MySQLdb
import sys


def main():
    """
    A script that accesses a mysql database
    """
    interf = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )
    state_name = sys.argv[4] if sys.argv[4] is not None else None
    ses = interf.cursor()

    ses.execute(
        "SELECT * FROM states \
            WHERE BINARY name = %s",
        (state_name,),
    )

    result = ses.fetchall()

    for r in result:
        print(r)

    ses.close()
    interf.close()


if __name__ == "__main__":
    main()
