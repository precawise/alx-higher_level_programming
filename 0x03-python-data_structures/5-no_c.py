#!/usr/bin/python3
def no_f(my_string):
    return my_string.translate({ord(ch): None for ch in 'fF'})
