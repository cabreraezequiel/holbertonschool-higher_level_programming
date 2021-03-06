#!/usr/bin/python3
def print_square(size):
    """adds two integers or floats, casting floats into integers"""

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print("")
