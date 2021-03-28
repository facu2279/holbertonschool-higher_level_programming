#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for estado in session.query(State).order_by(State.id):
        print(estado.id, end="")
        print(":", estado.name)
        for city in session.query(City).filter(City.state_id == estado.id):
            print("    ", city.id, end="")
            print(":", city.name)
