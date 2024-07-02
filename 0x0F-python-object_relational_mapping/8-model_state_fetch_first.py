#!/usr/bin/python3

"""
A script that prints the first State object from the database
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import sys


def main():
    """
    Connects to a database and prints the first State object
    """
    user = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]

    connection_uri = f"mysql://{user}:{password}@localhost:3306/{database}"

    engine = create_engine(connection_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Base.metadata.create_all(engine)

    state = session.query(State).order_by(State.id).first()

    print(f"{state.id}: {state.name}" if state is not None else "Nothing")


if __name__ == "__main__":
    main()
