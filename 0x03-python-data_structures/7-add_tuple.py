#!/usr/bin/python3
def add_tuple(tuple_x=(), tuple_y=()):
    new_tuple = ()
    tuple_x += (0, 0)
    tuple_y += (0, 0)
    new_tuple = tuple_x[0] + tuple_y[0], tuple_x[1] + tuple_y[1]
    return new_tuple
