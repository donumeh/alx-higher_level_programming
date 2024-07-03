#!/usr/bin/python3

"""
A script that creates the state "California" with the City
San Francisco" for a database
"""

import sys
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    """
    Script to create different records in database
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    session.add(cali)
    session.commit()

    san_fr = City(state_id=cali.id, name="San Francisco")
    session.add(san_fr)

    session.commit()

    session.close()


if __name__ == "__main__":
    main()
