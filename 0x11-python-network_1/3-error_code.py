#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021"""

import urllib.error as error
import urllib.request as llamada
from sys import argv

if __name__ == "__main__":
    datos = llamada.Request(argv[1])
    try:
        with llamada.urlopen(datos) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
