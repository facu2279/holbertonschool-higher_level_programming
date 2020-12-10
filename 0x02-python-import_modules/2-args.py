#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{}".format("0 arguments."))
    elif len(sys.argv) == 2:
        print("{}".format("1 argument:"))
        print("{:d}{}{}".format(1, ": ", sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        i = 0
        for i in range(len(sys.argv) - 1):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
