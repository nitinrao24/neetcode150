# leetcode 84
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1
# return the area of the largest rectangle in the histogram.

# Time Complexity: O(n)
# Space Complexity: O(n)

def largestRectangleInHistogram(heights):
    indices = [-1]
    best = 0
    n = len(heights)

    for idx in range(n):
        while indices[-1] != -1 and heights[idx] <= heights[indices[-1]]:
            top = indices.pop()
            h = heights[top]
            w = idx - indices[-1] - 1
            area = h * w
            if area > best:
                best = area
        indices.append(idx)

    while indices[-1] != -1:
        top = indices.pop()
        h = heights[top]
        w = n - indices[-1] - 1
        area = h * w
        if area > best:
            best = area

    return best

print(largestRectangleInHistogram([2,1,5,6,2,3]))