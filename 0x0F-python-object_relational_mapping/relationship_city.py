#!/usr/bin/python3
""" 14. Cities in state """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base

class City(Base):
    """
        definition of a City table
        Attributes:
            id (int): integer represent city id
            name (str): string represent the name of the city
            state_id (int): a reference to states table.

    """
    __tablename__ = "cities"

    id = Column(
            'id', Integer, unique=True,
            nullable=False, primary_key=True, autoincrement=True
            )
    name = Column('name', String(128), nullable=False)
    state_id = Column(
            'state_id', Integer, ForeignKey("states.id"), nullable=False
            )
    states = relationship("State", back_populates="cities")
