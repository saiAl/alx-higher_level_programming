#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_states():
    """ lists all State objects from the database """

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    for col in session.query(State).order_by(State.id):
        print("{}: {}".format(col.id, col.name))


if '__name__' == '__main__':
    list_states()
