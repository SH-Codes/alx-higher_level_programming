#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a modified binary search.

    Args:
        list_of_integers (list): List of integers to find a peak of.

    Returns:
        int or None: Peak of list_of_integers if found, None otherwise.
    """
    size = len(list_of_integers)
    
    # Edge case: Empty list
    if size == 0:
        return None
    
    # Perform binary search to find peak
    left, right = 0, size - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Peak must be on the right side
            left = mid + 1
        else:
            # Peak must be on the left side (or at mid)
            right = mid
    
    # Peak found at left or right index
    return list_of_integers[left]
