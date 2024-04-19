#!/usr/bin/python3
"""script that creates State with the City"""
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
    # create the tables in the database.
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add_all([state, city])
    session.commit()
    session.close()
