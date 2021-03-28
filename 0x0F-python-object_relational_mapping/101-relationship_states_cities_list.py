#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import State
from relationship_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for estado in session.query(State).order_by(State.id):
        print("{}: {}".format(estado.id, estado.name))
        for city in estado.cities:
            print("\t{}: {}".format(city.id, city.name))
