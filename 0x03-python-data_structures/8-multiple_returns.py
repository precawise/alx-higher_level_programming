#!/usr/bin/python3
def multiple_returns(string):
    if len(string) == 0:
        return 0, None
    else:
        return len(string), string[0]
