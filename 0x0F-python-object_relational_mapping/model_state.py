#!/usr/bin/python3
""" 6. First state model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
        class that represents state table

        Attributes:
            id (int): a unique number for each state.
            name (str): a string represents of the state.

    """

    __tablename__ = "states"
    id = Column(
            'id', Integer, primary_key=True,
            autoincrement=True, nullable=False, unique=True
            )
    name = Column('name', String(128), nullable=False)
