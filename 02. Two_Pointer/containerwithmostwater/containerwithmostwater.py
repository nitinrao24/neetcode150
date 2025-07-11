# leetcode 11
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

def containerWithMostWater(heights):
    best_area = 0
    left_idx = 0
    right_idx = len(heights) - 1

    while left_idx < right_idx:
        width = right_idx - left_idx
        min_height = min(heights[left_idx], heights[right_idx])
        area = width * min_height
        best_area = max(best_area, area)

        if heights[left_idx] < heights[right_idx]:
            left_idx += 1
        else:
            right_idx -= 1

    return best_area

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))