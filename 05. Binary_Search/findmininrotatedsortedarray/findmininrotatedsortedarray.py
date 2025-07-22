# leetcode 153
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# Time Complexity:
# Space Complexity:

def findMinInRotatedSortedArray(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if nums[mid] <= nums[end]:
            end = mid
        else:
            start = mid + 1

    return nums[start]

print(findMinInRotatedSortedArray([3,4,5,1,2]))