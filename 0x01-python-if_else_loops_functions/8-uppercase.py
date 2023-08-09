#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) <= ord('z') and ord(char) >= ord('a'):
            new_char = chr(ord(char) - 32)
        else:
            new_char = char
        print("{:s}".format(new_char), end="")
    print('')
