#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(save, size=0, position=(0, 0)) -> None:
        """
        Intializes the attributes

        Args:
            size: size of square
            position:  position of square
        """
        save.size = size
        save.position = position

    @property
    def size(save):
        """ Gets the private attribute to be used in class """
        return save.__size

    @size.setter
    def size(save, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            save.__size = value

    @property
    def position(save):
        """ Gets the private attribute to be used in class """
        return save.__position

    @position.setter
    def position(save, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            save.__position = value     # tuple contains 2 positive integers

    def area(save):
        """ Computes area of a square """
        return save.__size ** 2

    def my_print(save):
        """ Prints in stdout the square with the character # """
        if save.__size == 0:
            print()
        else:
            integer = 0
            pos1, pos2 = save.__position
            for new_line in range(pos2):
                print()
            while integer < save.__size:

                m = 0
                while m < pos1:
                    print(" ", end='')  # replace position with space
                    m += 1

                number = 0
                while number < save.__size:
                    print("{}".format("#"), end='')
                    number += 1
                print()
                integer += 1
