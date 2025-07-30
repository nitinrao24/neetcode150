# leetcode 239
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

# Time Complexity: O(n)
# Space Complexity: O(k)

def slidingWindowMax(nums, k):
    from collections import deque

    result = []  # this will store the max of each window
    window = deque()  # our deque will store elements of the current window

    for i in range(len(nums)):  # iterate over each index in nums
        num = nums[i]  # the current number

        # remove all smaller numbers from the back
        # since they cannot be the max if current num is larger
        while window and window[-1] < num:
            window.pop()  # pop smaller elements

        window.append(num)  # add current number to the back of the deque

        # once we've moved past the first k elements,
        # we need to remove the element that's sliding out of the window
        if i >= k and nums[i - k] == window[0]:
            window.popleft()  # remove it from the front if it's the same as the max

        # once we've filled our first full window (i >= k-1),
        # we can record the current max (front of deque)
        if i >= k - 1:
            result.append(window[0])

    return result  # return the list of maximums

print(slidingWindowMax([1,3,-1,-3,5,3,6,7],3))