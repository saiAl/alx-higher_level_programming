#!/usr/bin/python3
""" 11. Add a new state """
from sqlalchemy import create_engine, insert
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    url = URL.create(
            "mysql+mysqldb", usrname,
            passwd, "localhost",
            3306, db
            )

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    states = session.query(State.id, State.name).order_by(State.id)
    for state in states:
        print(f"{state[0]: state[1]}")

    session.close()
