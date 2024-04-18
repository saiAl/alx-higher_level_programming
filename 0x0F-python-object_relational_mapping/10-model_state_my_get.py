#!/usr/bin/python3
""" 10. Get a state """
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    usr_input = sys.argv[4]

    url = URL.create(
            "mysql+mysqldb", usrname,
            passwd, "localhost",
            3306, db
            )

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(
            State.id, State.name
            ).order_by(State.id)

    output = None
    for state in states:
        if state[1] == usr_input:
            output = state[0]

    if output is None:
        output = "Not found"
    print(output)

    session.close()
