#!/usr/bin/python3

"""
A script that lists all State objects
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def main():
    """
    Connects to a data base and returns some values
    """
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{} \
                ".format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bing=engine)
    session = Session()

    states = session.query(State).order_by(states.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
