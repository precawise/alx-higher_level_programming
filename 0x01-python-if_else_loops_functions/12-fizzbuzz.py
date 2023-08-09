#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        output = ""
        if a % 3 == 0:
            output += "Fizz"
        if a % 5 == 0:
            output += "Buzz"
        if output == "":
            output = a
        print(output, end=" ")
