#!/usr/bin/python3
for i in range(9):
    for i2 in range(10):
        if i < i2:
            print('{:d}{:d}, '.format(i, i2), end="")
print("89")
