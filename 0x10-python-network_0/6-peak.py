#!/usr/bin/python3
"""This module defines the function find_peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Get the peak of a list"""

    if not list_of_integers:
        return None
    lenght = len(list_of_integers)
    return find_peak_until(list_of_integers, 0, lenght - 1, lenght)


def find_peak_until(li, low, high, n):
    """Function that returns a peak of a list of integers"""
    middle = int(low + (high - low) / 2)

    if (middle == 0 or li[middle] >= li[middle - 1]) and \
       (middle == n - 1 or li[middle] >= li[middle + 1]):
        return li[middle]
    elif middle > 0 and li[middle] < li[middle - 1]:
        return find_peak_until(li, low, middle - 1, n)
    else:
        return find_peak_until(li, middle + 1, high, n)
