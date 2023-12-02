#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    import os
    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        os._exit(1)
    op = sys.argv[2]
    if op not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        os._exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result))
