#!/usr/bin/python3
for letter in range(100):
    if letter == 99:
        print(letter)
    else:
        print("{:0>2d}".format(letter), end=", ")
