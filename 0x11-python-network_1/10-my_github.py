#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
import sys

if __name__ == "__main__":
    userxd = sys.argv[1]
    passxd = sys.argv[2]
    link = "https://api.github.com/user"
    res = requests.get(link, auth=(userxd, passxd))
    print(res.json().get('id'))
