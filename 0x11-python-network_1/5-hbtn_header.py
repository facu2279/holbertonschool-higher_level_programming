#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
