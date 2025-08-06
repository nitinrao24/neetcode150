# leetcode 4
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Time Complexity: O(log min(len(arr1), len(arr2)))
# Space Complexity: O(1)

from typing import List

def find_median_sorted_arrays(arr1: List[int], arr2: List[int]) -> float:
    """
    Find the median of two sorted arrays
    """

    # Always do binary search on the smaller array to keep runtime minimal
    if len(arr1) > len(arr2):
        return find_median_sorted_arrays(arr2, arr1)

    n1, n2 = len(arr1), len(arr2)
    low, high = 0, n1

    # Continue until we find the perfect partition
    while low <= high:
        # cut1 is how many elements we take from arr1's left side
        cut1 = (low + high) // 2
        # cut2 complements cut1 so that left halves total half of all elements
        cut2 = (n1 + n2 + 1) // 2 - cut1

        # If cut1 is 0, left_max_1 = -infinity (no elements on left side)
        left_max_1  = arr1[cut1 - 1] if cut1  > 0 else float('-inf')
        # If cut1 is n1, right_min_1 = +infinity (no elements on right side)
        right_min_1 = arr1[cut1]     if cut1  < n1 else float('inf')

        # Same logic for arr2
        left_max_2  = arr2[cut2 - 1] if cut2  > 0 else float('-inf')
        right_min_2 = arr2[cut2]     if cut2  < n2 else float('inf')

        # Check if we have a valid partition:
        # all left-side elements ≤ all right-side elements
        if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
            # If total number of elements is even, median is average of two middle values
            if (n1 + n2) % 2 == 0:
                return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2
            # If odd, median is the max of the left halves
            return max(left_max_1, left_max_2)

        # If left_max_1 is too big, we need to move cut1 to the left
        if left_max_1 > right_min_2:
            high = cut1 - 1
        else:
            # Otherwise, move cut1 to the right
            low = cut1 + 1

