#!/usr/bin/python3

"""
A script that adds a State object to the database
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import sys


def main():
    """
    Adds a state object to the database
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    lous = State(name="Louisiana")
    session.add(lous)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()

    print(f"{state.id}")


if __name__ == "__main__":
    main()
