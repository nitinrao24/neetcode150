# leetcode 198
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed
# ,the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Time Complexity:
# Space Complexity:

def houseRobber(nums):
    length = len(nums)

    if length == 1:
        return nums[0]

    best = [0] * length
    best[0] = nums[0]
    best[1] = max(nums[0], nums[1])

    for idx in range(2, length):
        skip = best[idx - 1]
        take = nums[idx] + best[idx - 2]
        best[idx] = max(skip, take)

    return best[-1]

print(houseRobber([1,2,3,1]))