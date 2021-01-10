#!/usr/bin/python3
def text_indentation(text):
    if not type(text) is str:
        raise TypeError("text must be a string")
    else:
        text = text.replace(". ", ".@")
        text = text.replace(": ", ":@")
        text = text.replace("? ", "?@")
        text = text.replace("@", "\n\n")

        print("{}".format(text), end="")
