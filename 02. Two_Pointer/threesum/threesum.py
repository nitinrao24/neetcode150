# leetcode 15
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def threeSum(nums):
    triplets = []
    nums.sort()

    for first in range(len(nums)):
        if first > 0 and nums[first] == nums[first - 1]:
            continue

        second = first + 1
        third = len(nums) - 1

        while second < third:
            current_sum = nums[first] + nums[second] + nums[third]

            if current_sum > 0:
                third -= 1
            elif current_sum < 0:
                second += 1
            else:
                triplets.append([nums[first], nums[second], nums[third]])
                second += 1
                while second < third and nums[second] == nums[second - 1]:
                    second += 1

    return triplets

print(threeSum([-1,0,1,2,-1,-4]))