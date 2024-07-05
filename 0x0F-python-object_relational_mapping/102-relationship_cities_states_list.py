#!/usr/bin/python3

"""
A script that lists all City objects from db
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from relationship_city import City
from relationship_state import State, Base


def main():
    """
    Connects to a db and prints all cities
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    counter = 1
    for city, state in result:
        print(f"{counter}: {city.name} -> {state.name}")
        counter += 1


if __name__ == "__main__":
    main()
