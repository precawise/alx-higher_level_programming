#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(save, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        save.size = size

    @property
    def size(save):
        """Get/set the current size of the square."""
        return (save.__size)

    @size.setter
    def size(save, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        save.__size = value

    def area(save):
        """Return the current area of the square."""
        return (save.__size * self.__size)

    def __eq__(save, other):
        """Define the == comparision to a Square."""
        return save.area() == other.area()

    def __ne__(save, other):
        """Define the != comparison to a Square."""
        return save.area() != other.area()

    def __lt__(save, other):
        """Define the < comparison to a Square."""
        return save.area() < other.area()

    def __le__(save, other):
        """Define the <= comparison to a Square."""
        return save.area() <= other.area()

    def __gt__(save, other):
        """Define the > comparison to a Square."""
        return save.area() > other.area()

    def __ge__(save, other):
        """Define the >= compmarison to a Square."""
        return save.area() >= other.area()
