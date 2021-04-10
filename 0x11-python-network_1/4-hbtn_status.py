#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
import requests

if __name__ == "__main__":
    url = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.content.decode('utf-8')))
