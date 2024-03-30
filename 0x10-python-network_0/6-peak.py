def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a simplified approach.

    Args:
        list_of_integers (list): List of integers to find a peak of.

    Returns:
        int or None: Peak of list_of_integers if found, None otherwise.
    """
    size = len(list_of_integers)

    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]

    # Compare middle element with its neighbors
    mid = size // 2
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) \
            and (mid == size - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        # Search left half if left neighbor is larger
        return find_peak(list_of_integers[:mid])
    else:
        # Search right half if right neighbor is larger
        return find_peak(list_of_integers[mid + 1:])
