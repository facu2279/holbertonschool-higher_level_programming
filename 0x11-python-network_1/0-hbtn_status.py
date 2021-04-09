#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import urllib.request as llamada

if __name__ == "__main__":
    with llamada.urlopen('https://intranet.hbtn.io/status') as res:
        datos = res.read()
        print('Body response:')
        print("\t- type: {}".format(type(datos)))
        print("\t- content: {}".format(datos))
        print("\t- utf8 content: {}".format(datos.decode('utf-8')))
