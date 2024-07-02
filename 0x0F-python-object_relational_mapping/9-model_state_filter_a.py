#!/usr/bin/python3

"""
A script that lists all State object that contain the letter `a`
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus
import sys


def main():
    """
    A script tha list all states objects that contains the letter `a`
    """

    user = sys.argv[1]
    password = quote_plus(sys.argv[2])
    database = sys.argv[3]

    connection_url = f"mysql://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(connection_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like("%a%"))

    states = query.order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
