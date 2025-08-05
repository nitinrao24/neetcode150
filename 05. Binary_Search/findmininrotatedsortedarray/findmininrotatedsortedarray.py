# leetcode 153
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

def find_min(nums: List[int]) -> int:
    """
    Find the minimum value in a rotated sorted list.
    Uses binary search to run in O(log n) time and O(1) space.
    """
    # Set two pointers at the ends of the list
    left = 0
    right = len(nums) - 1

    # Keep narrowing the range until the pointers meet
    while left < right:
        # Look at the middle element of the current range
        mid = (left + right) // 2

        # If the middle is less than or equal to the right end,
        # the smallest value must be at mid or to the left of it.
        if nums[mid] <= nums[right]:
            right = mid
        else:
            # Otherwise, the smallest value is strictly to the right of mid
            left = mid + 1

    # When left == right, that's the minimum element
    return nums[left]

print(find_min([3,4,5,1,2]))