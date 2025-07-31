# leetcode 416
# Given an integer array nums, return true if you can partition the array into two subsets
# such that the sum of the elements in both subsets is equal or false otherwise.
# Time Complexity:
# Space Complexity:

def partitionEqualSubsequence(nums):
    # compute total sum of all numbers
    total_sum = sum(nums)

    # if total is odd, cannot split into two equal subsets
    if total_sum % 2 == 1:
        return False

    # target sum for each subset
    half = total_sum // 2

    # dp[t] will be True if some subset sums to t
    can_reach = [False] * (half + 1)
    can_reach[0] = True  # zero is always reachable (empty subset)

    # try to build reachable sums using each number
    for value in nums:
        # iterate backwards to avoid reusing the same number in this iteration
        for t in range(half, value - 1, -1):
            if not can_reach[t] and can_reach[t - value]:
                can_reach[t] = True

        # early exit: if half is reachable, we can form two equal subsets
        if can_reach[half]:
            return True

    # final answer: whether half-sum is achievable
    return False

