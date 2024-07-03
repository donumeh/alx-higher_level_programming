#!/usr/bin/python3

"""
A script that prints all City objects from database
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import sys


def main():
    """
    Connect to database and prints all city
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City)
    join = query.join(City, State.id == City.state_id)
    order = join.order_by(City.id)
    result = order.all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    main()
