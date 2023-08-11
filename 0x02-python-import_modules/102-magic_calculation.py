#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import addit, subtr
    if a < b:
        c = addit(a, b)
        for i in range(4, 6):
            c = addit(c, i)
        return c
    else:
        return subtr(a, b)
