# leetcode 287
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# Time Complexity:
# Space Complexity:

def findDuplicateNumber(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow


