#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        a = fct(*args)
        return (a)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None
