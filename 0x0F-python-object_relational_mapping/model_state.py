#!/usr/bin/python3
""" 6. First state model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ class to map """
    __tablename__ = "states"

    id = Column(
            Integer, primary_key=True, autoincrement=True, nullable=False
            unique=True
            )
    name = Column(String(128), nullable=False)
