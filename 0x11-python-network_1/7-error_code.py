#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School """
import requests
from sys import argv

if __name__ == '__main__':
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
