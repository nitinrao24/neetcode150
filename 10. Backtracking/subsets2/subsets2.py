# leetcode 90
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Time Complexity:
# Space Complexity:
def subsets2(nums):
    all_subsets = []
    current_subset = []
    nums.sort()

    def backtrack(index):
        if index == len(nums):
            all_subsets.append(current_subset[:])
            return

        current_subset.append(nums[index])
        backtrack(index + 1)
        current_subset.pop()

        next_index = index
        while next_index + 1 < len(nums) and nums[next_index] == nums[next_index + 1]:
            next_index += 1

        backtrack(next_index + 1)

    backtrack(0)
    return all_subsets
print(subsets2([1,2,2]))