# leetcode 55
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

def jumpGame(nums):
    last_pos = len(nums) - 1

    for idx in range(len(nums) - 2, -1, -1):
        if idx + nums[idx] >= last_pos:
            last_pos = idx

    return last_pos == 0

print(jumpGame([2,3,1,1,4]))
print(jumpGame([3,2,1,0,4]))