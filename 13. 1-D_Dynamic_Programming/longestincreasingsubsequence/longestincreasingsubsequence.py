# leetcode 300
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Time Complexity:
# Space Complexity:

def longestIncreasingSubsequence(nums):
    tails = []

    def binary_search(arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    for num in nums:
        if not tails or tails[-1] < num:
            tails.append(num)
        else:
            pos = binary_search(tails, num)
            tails[pos] = num

    return len(tails)

print(longestIncreasingSubsequence([10,9,2,5,3,7,101,18]))