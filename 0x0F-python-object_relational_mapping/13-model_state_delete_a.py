#!/usr/bin/python3
""" 13. Delete states """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from model_state import Base, State
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

    states = session.query(State).filter(
            State.name.like("%a%")
            ).delete(synchronize_session=False)

    session.commit()
    session.close()
