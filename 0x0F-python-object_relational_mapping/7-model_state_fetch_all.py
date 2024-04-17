#!/usr/bin/python3
""" 7. All states via SQLAlchemy """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(
            State.id, State.name
            ).order_by(State.id)

    for state in states:
        print(f"{state[0]}: {state[1]}")

session.close()
