# leetcode 152
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# Time Complexity:
# Space Complexity:

def maxProductSubArray(nums):
    result = max(nums)
    mx = 1
    mn = 1

    for num in nums:
        prod1 = mx * num
        prod2 = mn * num

        mx = max(prod1, prod2, num)
        mn = min(prod1, prod2, num)

        if mx > result:
            result = mx

    return result

print(maxProductSubArray([2,3,-2,4]))