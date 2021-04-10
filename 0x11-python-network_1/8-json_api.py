#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        xd = argv[1]
    else:
        xd = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'xd': xd})
    try:
        r_dict = res.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
