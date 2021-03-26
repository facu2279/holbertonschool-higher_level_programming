#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

if __name__ == "__main__":

    from sys import argv
    import MySQLdb
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    nuevaconexion = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT * FROM states")
    resultado = consulta.fetchall()
    for fila in resultado:
        print(fila)
    nuevaconexion.close()
