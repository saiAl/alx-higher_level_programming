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

    states = session.query(
            State.id, State.name).order_by(State.id)
    cities = session.query(
            City.id, City.name, City.state_id).order_by(City.id)

    for state in states:
        print(f"{state[0]}: {state[1]}")
        for city in cities:
            if city[2] == state[0]:
                print(f"\t{city[0]}: {city[1]}")
            else:
                continue
