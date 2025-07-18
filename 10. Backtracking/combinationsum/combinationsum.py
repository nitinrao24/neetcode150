# leetcode 39
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# Time Complexity:
# Space Complexity:

def combinationSum(candidates, target):
    combinations = []

    def search(start_index, path, current_sum):
        if current_sum == target:
            combinations.append(path[:])
            return

        if current_sum > target:
            return

        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            search(i, path, current_sum + candidates[i])
            path.pop()

    search(0, [], 0)
    return combinations

print(combinationSum([2,3,6,7],7))