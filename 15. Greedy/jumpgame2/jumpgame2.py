# leetcode 45
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i],
# you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n

def jumpGameTwo(nums):
    current_start = 0
    current_end = 0
    jump_count = 0

    while current_end < len(nums) - 1:
        furthest_reach = 0

        for idx in range(current_start, current_end + 1):
            reach = idx + nums[idx]
            if reach > furthest_reach:
                furthest_reach = reach

        current_start = current_end + 1
        current_end = furthest_reach
        jump_count += 1

    return jump_count

print(jumpGameTwo([2,3,1,1,4]))