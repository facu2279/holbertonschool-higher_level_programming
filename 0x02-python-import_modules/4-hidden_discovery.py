#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = dir(hidden_4)
    for i in range(len(a)):
        if a[i][:2] != "__":
            print("{}".format(a[i]))
