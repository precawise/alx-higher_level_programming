#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
    
    print("Sum: {}".format(total))
