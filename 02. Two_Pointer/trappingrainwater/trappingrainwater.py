# leetcode 42
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Time Complexity:
# Space Complexity:

def trappingRainWater(height):
    left_ptr = 0
    right_ptr = len(height) - 1

    max_left = height[left_ptr]
    max_right = height[right_ptr]

    total_water = 0

    while left_ptr < right_ptr:
        if max_left < max_right:
            left_ptr += 1
            current_height = height[left_ptr]
            max_left = max(max_left, current_height)
            total_water += max_left - current_height
        else:
            right_ptr -= 1
            current_height = height[right_ptr]
            max_right = max(max_right, current_height)
            total_water += max_right - current_height

    return total_water

print(trappingRainWater([4,2,0,3,2,5]))