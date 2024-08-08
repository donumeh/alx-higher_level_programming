#!/usr/bin/python3


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def binary_search_peak(nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            return binary_search_peak(nums, mid + 1, high)
        else:
            return binary_search_peak(nums, low, mid)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
