#!/usr/bin/python3
""" 14. Cities in state """
from state_model import Base
from sqlalchemy import Column, String, Integer, ForeginKey


class City(Base):
    """ definition of a City table """
    __tablename__ = "cities"

    id = Column(
            Integer, unique=True,
            nullable=False, primary_key=True, autoincrement=True
            )
    name = (
            String(128), nullable=False
            )
    state_id = (
            ForeignKey("State.id"), Integer, nullable=False
            )
