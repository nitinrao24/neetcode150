# leetcode 128
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Time Complexity:
# Space Complexity:

def longestConsecutiveSequence(nums):
    s = set(nums)
    best = 0

    for n in s:
        if n - 1 not in s:
            cur = 1
            while n + cur in s:
                cur += 1
            best = max(best, cur)

    return best

print(longestConsecutiveSequence([100,4,200,1,3,2]))