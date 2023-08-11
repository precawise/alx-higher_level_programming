#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5

    add_result = calc.add(a, b)
    sub_result = calc.sub(a, b)
    mul_result = calc.mul(a, b)
    div_result = calc.div(a, b)

        print("{} + {} = {}".format(a, b, add_result))
        print("{} - {} = {}".format(a, b, sub_result))
        print("{} * {} = {}".format(a, b, mul_result))
        print("{} / {} = {}".format(a, b, div_result))
