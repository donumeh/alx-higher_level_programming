#!/usr/bin/python3

"""
A script that lists all State objects
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import sys


def main():
    """
    Connects to a data base and returns some values
    """
    user = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]

    connection_uri = f"mysql://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(connection_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
