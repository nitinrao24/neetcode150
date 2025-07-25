# leetcode 213
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Time Complexity:
# Space Complexity:

def houseRobber2(nums):
    def get_max(houses):
        previous = 0
        current = 0

        for val in houses:
            new_max = max(current, previous + val)
            previous = current
            current = new_max

        return current

    case1 = get_max(nums[:-1])
    case2 = get_max(nums[1:])
    case3 = nums[0]

    result = max(case1, case2, case3)
    return result

print(houseRobber2([2,3,2]))