#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats")
    
    return int(a) + int(b)
