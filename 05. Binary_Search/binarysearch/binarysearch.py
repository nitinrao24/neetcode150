# leetcode 704
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Time Complexity:
# Space Complexity:

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1

print(binarySearch([-1,0,3,5,9,12],9))
print(binarySearch([-1,0,3,5,9,12],2))