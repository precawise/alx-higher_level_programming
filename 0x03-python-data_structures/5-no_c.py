#!/usr/bin/python3
def no_d(my_string):
    my_str = [ch for ch in my_string if ch != 'd' and ch != 'D']
    return ''.join(my_str)
