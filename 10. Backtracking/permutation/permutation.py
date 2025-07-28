# leetcode 46
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Time Complexity:
# Space Complexity:

def permutation(nums):
    def backtrack(index):
        if index == len(nums):
            permutations.append(nums[:])
            return

        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            backtrack(index + 1)
            nums[index], nums[j] = nums[j], nums[index]

    permutations = []
    backtrack(0)
    return permutations

print(permutation([1,2,3]))