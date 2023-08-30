#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(save, radius=0):
        """Initialize a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        save.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        save.__radius = radius

    def area(save):
        """Return the area of the MagicClass."""
        return (save.__radius ** 2 * math.pi)

    def circumference(save):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * save.__radius)
