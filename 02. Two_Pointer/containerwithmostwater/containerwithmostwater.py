# leetcode 11
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Time Complexity: O(n)
# Space Complexity: O(1)

def containerWithMostWater(self, height: List[int]) -> int:
    # Start with zero as the best (largest) area we’ve seen
    best_area = 0

    # Place one pointer at the very left, one at the very right
    left = 0
    right = len(height) - 1

    # Keep going until the two pointers meet
    while left < right:
        # Width of the container is the distance between pointers
        width = right - left

        # Height of the container is the smaller of the two lines
        if height[left] < height[right]:
            current_height = height[left]
        else:
            current_height = height[right]

        # Area = width × height
        area = width * current_height

        # If this area is larger than any we’ve seen, remember it
        if area > best_area:
            best_area = area

        # Move the pointer on the shorter line inward,
        # because only by finding a taller line could we possibly increase area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # After the loop, best_area holds the maximum possible
    return best_area

def containerWithMostWater1(heights):
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