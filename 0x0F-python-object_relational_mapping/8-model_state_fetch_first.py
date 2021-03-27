#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_element = session.query(State).filter(State.id == 1).first()
    print(first_element.id, end="")
    print(": ", end="")
    print(first_element.name)
