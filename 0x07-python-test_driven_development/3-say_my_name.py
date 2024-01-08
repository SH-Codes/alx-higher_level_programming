#!/usr/bin/python3

"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not all(isinstance(name, str) for name in (first_name, last_name)):
        raise TypeError("Both first_name and last_name must be strings")
    
    print("My name is {} {}".format(first_name, last_name))
