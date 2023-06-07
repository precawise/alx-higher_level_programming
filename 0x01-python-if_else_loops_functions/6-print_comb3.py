#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(chr(i + 48), chr(j + 48)))
        else:
            print("{}{}".format(chr(i + 48), chr(j + 48)), end=", ")
