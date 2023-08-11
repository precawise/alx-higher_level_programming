#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import result_add, result_sub, result_mul, result_div
    import sys
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, result_add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, result_sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, result_mul(a, b)))
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, result_div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
