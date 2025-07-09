# leetcode 739
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day
# to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Time Complexity:
# Space Complexity:

def dailyTemperatures(nums):
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