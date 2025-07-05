# leetcode 136
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Time Complexity:
# Space Complexity:
def singleNumber(nums):
    seen = set()
    for n in nums:
        if n in seen:
            seen.remove(n)
        else:
            seen.add(n)
    return seen.pop()

print(singleNumber([1]))
