#!/usr/bin/python3
""" 6. First state model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class Base(declarative_base):
    """class which maintains a catalog"""
    pass


class State(Base):
    """ class to map """
    __tablename__ = 'states'

    id = Column(
            'id', Integer, primary_key=True, autoincrement=True, nullable=False
            )
    name = Column('name', String(128), nullable=False)
