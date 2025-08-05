# leetcode 312
# You are given n balloons, indexed from 0 to n - 1.
# Each balloon is painted with a number on it represented by an array nums.
# You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
# If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Time Complexity:
# Space Complexity:
from typing import List
def maxCoins(self, nums: List[int]) -> int:
    # Add sentinel balloons (value 1) at both ends to simplify edge calculations
    arr = [1] + nums + [1]
    memo = {}  # cache results for subproblems

    def dfs(left: int, right: int) -> int:
        # Base case: no balloons in this interval
        if left > right:
            return 0

        # Return cached result if available
        if (left, right) in memo:
            return memo[(left, right)]

        max_coins = 0
        left_val = arr[left - 1]    # value of balloon immediately before interval
        right_val = arr[right + 1]  # value of balloon immediately after interval

        # Try bursting each balloon i last in [left..right]
        for i in range(left, right + 1):
            # coins gained by bursting balloon i between left_val and right_val
            coins = arr[i] * left_val * right_val

            # coins from bursting all balloons to the left of i
            coins += dfs(left, i - 1)

            # coins from bursting all balloons to the right of i
            coins += dfs(i + 1, right)

            # track the best possible outcome
            if coins > max_coins:
                max_coins = coins

        # cache and return the best result for this interval
        memo[(left, right)] = max_coins
        return max_coins

    # start with the full range of real balloons (exclude the added sentinels)
    return dfs(1, len(arr) - 2)