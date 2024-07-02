#!/usr/bin/python3

"""
Write a script that prints the State object with the
name passed as arg
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from model_state import Base, State


def main():
    """
    connects to a database to prints the names of arg passed
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]
    state_name = sys.argv[4]

    connection_url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"
    engine = create_engine(connection_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == f"{state_name}")

    state = query.first()

    print(f"{state.id}" if state is not None else "Not found")


if __name__ == "__main__":
    main()
