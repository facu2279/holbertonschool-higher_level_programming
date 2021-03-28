#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """ Create class City """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
