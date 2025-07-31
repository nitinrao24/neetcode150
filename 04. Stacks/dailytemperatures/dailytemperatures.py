# leetcode 739
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day
# to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    # Prepare answer array filled with 0s (default if no warmer day exists)
    ans = [0] * n
    # Stack will hold indices of days; temperatures at those indices are in decreasing order
    stack: List[int] = []

    # Iterate through each day
    for i in range(n):
        # While there is a previous day with a lower temperature than today
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()          # Get the index of that cooler day
            ans[prev_idx] = i - prev_idx    # Distance to the next warmer day
        # Push current day index onto stack for future comparisons
        stack.append(i)

    return ans

def dailyTemperatures1(nums):
    n = len(nums)
    ans = [0] * n
    stack = []

    for i in range(n):
        while stack and nums[i] > stack[-1][1]:
            index = stack.pop()[0]
            ans[index] = i - index
        stack.append((i, nums[i]))

    return ans

print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))
print(dailyTemperatures([73,74,75,71,69,72,76,73]))