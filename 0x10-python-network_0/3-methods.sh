#!/bin/bash
# Made by Facundo Diaz for Holberton School 2021
curl -sI GET $1 | grep "Allow" | cut -f2- -d " "

