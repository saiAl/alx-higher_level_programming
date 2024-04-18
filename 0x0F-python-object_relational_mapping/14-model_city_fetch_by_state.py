#!/usr/bin/python3
""" prints all City objects from the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from model_state import Base, State
from model_city import City
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

    resualt = session.query(
            State.name, City.id, City.name
            ).join(City).filter(State.id == City.state_id)

    for res in resualt:
        print(f"{res[0]}: ({res[1]}) {res[2]}")

    session.close()
