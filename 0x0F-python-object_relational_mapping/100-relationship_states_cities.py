#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """

from relationship_state import Base, State
from relationship_city import City
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
