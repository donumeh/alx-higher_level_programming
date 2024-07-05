#!/usr/bin/python3

"""
A script that list state objects and corresponding City objects
"""

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
    Connects to database and list all states and cities
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    uri = f"mysql://{usr}:{passwd}@localhost:3306/{db}"

    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(State)
        .join(City, State.id == City.state_id)
        .order_by(State.id, City.id)
        .all()
    )

    for state in result:
        print(f"{state.id}: {state.name}")

        for c in state.cities:
            print(f"\t{c.is}: {c.name}")


if __name__ == "__main__":
    main()
