#!/usr/bin/python3

import sys

args = sys.argv[1:]
num_args = len(args)

print("Number of argument(s):", num_args)
print("Argument{}:".format("s" if num_args != 1 else ""), end=" ")
print(", ".join(["{}: {}".format(i + 1, arg) for i, arg in enumerate(args)]) if num_args > 0 else ".", end="\n")
