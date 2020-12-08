#!/usr/bin/python3
for abc in reversed(range(97, 123)):
    if abc % 2 != 0:
        abc = abc - 32
    print("{}".format(chr(abc)), end="")
