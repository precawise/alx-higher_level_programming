#!/usr/bin/python3
def remove_char_at(string, n):
    new_string = ''
    for str, char in enumerate(string):
        if str != n:
            new_string += char
    return new_string
