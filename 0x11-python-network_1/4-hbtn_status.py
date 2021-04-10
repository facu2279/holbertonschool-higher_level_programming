#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School """
import requests

if __name__ == '__main__':
    data = requests.get('https://intranet.hbtn.io/status')
    res = data.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
