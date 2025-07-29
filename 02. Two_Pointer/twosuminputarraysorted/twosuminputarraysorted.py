# leetcode 167
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums,target):
    start_idx = 0
    end_idx = len(nums) - 1

    while start_idx < end_idx:
        current_sum = nums[start_idx] + nums[end_idx]

        if current_sum == target:
            return [start_idx + 1, end_idx + 1]
        elif current_sum > target:
            end_idx -= 1
        else:
            start_idx += 1

print(twoSum([2,7,11,15],9))