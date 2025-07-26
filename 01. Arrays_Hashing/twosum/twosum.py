# leetcode 1
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create an empty dictionary to remember numbers we've seen and their indices
    seen = {}
    # Go through each number in the list, keeping track of its position
    for index, number in enumerate(nums):
        # Figure out what number we need to reach the target when added to the current one
        complement = target - number
        # Check if that needed number is something we’ve already encountered
        if complement in seen:
            # If yes, return the index of the earlier number and the current index
            return [seen[complement], index]
        # Otherwise, save the current number and its index for future complements
        seen[number] = index
    # If we finish the loop without finding a pair, return an empty list
    return []

def twoSum1(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))