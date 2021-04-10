#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    link = 'https://api.github.com/user'
    linkxd = requests.get(link, auth=HTTPBasicAuth(argv[1], argv[2]))
    if linkxd.status_code == 200:
        dict = url.json()
        print(dict['id'])
    else:
        print("None")
