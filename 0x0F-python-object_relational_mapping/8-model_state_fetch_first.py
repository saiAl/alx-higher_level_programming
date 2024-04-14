#!/usr/bin/python3
""" 8. First state"""


if '__name__' == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3])
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(
            State.id, State.name
            ).where(State.id == 1)

    if (state.first() is not None):
        state_name = f"{state.first().id}: {state.first().name}"
        print(state_name)
    else:
        print("Nothing")

    session.close()
