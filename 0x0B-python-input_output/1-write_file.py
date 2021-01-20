#!/usr/bin/python3
def write_file(filename="", text=""):
    cont = 0
    with open(filename, "w") as file:
        for line in text:
            cont = cont + len(line)
        return (cont)
