# leetcode 53
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Time Complexity:
# Space Complexity:

def maximumSubArray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum

print(maximumSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maximumSubArray([-1]))