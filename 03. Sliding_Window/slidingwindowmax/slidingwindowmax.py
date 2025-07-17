# leetcode 239
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

# Time Complexity:
# Space Complexity:

def slidingWindowMax(nums, k):
    from collections import deque

    result = []
    window = deque()

    for i in range(len(nums)):
        num = nums[i]

        while window and window[-1] < num:
            window.pop()
        window.append(num)

        if i >= k and nums[i - k] == window[0]:
            window.popleft()

        if i >= k - 1:
            result.append(window[0])

    return result

print(slidingWindowMax([1,3,-1,-3,5,3,6,7],3))