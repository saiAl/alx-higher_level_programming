#!/usr/bin/python3
"""
    script that lists all State objects,
    and corresponding City objects
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import sys


if __name__ == '__main__':
    url = URL.create(
            "mysql+mysqldb", sys.argv[1],
            sys.argv[2], "localhost",
            3306, sys.argv[3]
            )

    engine = create_engine(url)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
