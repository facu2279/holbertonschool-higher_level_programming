#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import urllib.request as llamada
from sys import argv

if __name__ == "__main__":
    datos = llamada.Request(argv[1])
    with llamada.urlopen(datos) as res:
        print(res.headers.get('X-Request-Id'))
