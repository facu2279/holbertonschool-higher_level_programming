#!/usr/bin/python3
""" Made by Facundo Diaz to Holberton School 2021 """

if __name__ == "__main__":

    from sys import argv
    import MySQLdb
    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    argument = argv[4]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT * FROM states WHERE name ='{}'".format(argument))
    resultado = consulta.fetchall()
    for fila in resultado:
        if fila[1] == argument:
            print(fila)
    nuevaconexion.close()
