#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        signo = sys.argv[2]
        if signo == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif signo == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif signo == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif signo == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)
    else:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
