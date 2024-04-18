#!/usr/bin/python3
""" 12. Update a state """
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
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

    states = session.query(
            State
            ).filter(State.id == 2).update(
                    {State.name: "New Mexico"}
                    )
    session.commit()
    session.close()
