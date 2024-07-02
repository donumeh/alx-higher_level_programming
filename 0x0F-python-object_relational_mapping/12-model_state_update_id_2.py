#!/usr/bin/python3

"""
A script that changes the name of a state
"""

import sys
from urllib.parse import quote_plus
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def main():

    """
    Connects to a database to update a record
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:

        state.name = "New Mexico"

        session.commit()


if __name__ == "__main__":
    main()
