#!/usr/bin/python3

"""
A script that deletes all State objects with a name containing letter a
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from model_state import Base, State


def main():
    """
    connects to db and deletes some records
    """

    usr = sys.argv[1]
    passwd = quote_plus(sys.argv[2])
    db = sys.argv[3]

    url = f"mysql://{usr}:{passwd}@localhost:3306/{db}"
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like("%a%"))
    query.delete(synchronize_session=False))
    
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
