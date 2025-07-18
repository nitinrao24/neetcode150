# leetcode 78
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Time Complexity:
# Space Complexity:

def subsets(nums):
    all_subsets = []
    current_subset = []

    def dfs(index):
        if index == len(nums):
            all_subsets.append(current_subset[:])
            return

        current_subset.append(nums[index])
        dfs(index + 1)

        current_subset.pop()
        dfs(index + 1)

    dfs(0)
    return all_subsets

print(subsets([1,2,3]))