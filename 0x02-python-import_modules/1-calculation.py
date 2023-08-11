#!/usr/bin/python3

if __name__ == "__main__":
	from calculator_1 import add_result, sub_result, mul_result, div
	a = 10
	b = 5
        print("{:d} + {:d} = {:d}".format(a, b, add_result))
        print("{:d} - {:d} = {:d}".format(a, b, sub_result))
        print("{:d} * {:d} = {:d}".format(a, b, mul_result))
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b))
