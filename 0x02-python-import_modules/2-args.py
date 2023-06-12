#!/usr/bin/python3
    if __name__ == "__main__":
    import sys
    num = len(sys.argv)

    if num == 1:
    print("{} arguments.".format(num - 1))
    elif num == 2:
    print("{} argument:".format(num - 1))
    else:
    print("{} arguments:".format(num - 1))

    for i in range(0, num - 2):
    print("{}: {}".format(i + 2, sys.argv[i + 2]))
