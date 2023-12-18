#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    if my_list is None:
        my_list = []

    elements_printed = 0

    for element in my_list[:x]:
        print("{}".format(element), end="")
        elements_printed += 1

    print("")
    return elements_printed
