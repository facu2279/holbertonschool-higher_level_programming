#!/bin/bash
# Made by Facundo Diaz for Holberton School
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
