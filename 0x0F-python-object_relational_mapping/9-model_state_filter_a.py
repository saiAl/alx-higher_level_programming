#!/usr/bin/python3
""" 9. Contains a """
from model_state import State, Base
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
            ).filter(
                    State.name.like("%a%")
                    ).order_by(State.id)
    for state in states:
        print(state)

    session.close()
