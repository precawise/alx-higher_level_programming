#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(save, size=0) -> None:
        """
        Intializes class attributes

        Args:
            size:   size of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            save.__size = size
