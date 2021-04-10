#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv
if __name__ == '__main__':
    res = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(res.json().get('id'))
