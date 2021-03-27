#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

from sys import argv
import MySQLdb

if __name__ == "__main__":

    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D, port=3306, charset="utf8")
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    resultado = consulta.fetchall()
    for fila in resultado:
        print(fila)
    consulta.close()
    nuevaconexion.close()
