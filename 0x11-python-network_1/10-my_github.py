#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    psw = sys.argv[2]
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(user, psw))
    print(res.json().get('id'))
