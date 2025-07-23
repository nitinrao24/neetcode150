# leetcode 937
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# Time Complexity:
# Space Complexity:

import random
from typing import List

def kClosestPoints(points,k):
    def squared_distance(point):
        x = point[0]
        y = point[1]
        dist = x * x + y * y
        return dist

    def partition(left, right, pivot_index):
        pivot_point = points[pivot_index]
        pivot_dist = squared_distance(pivot_point)

        temp = points[pivot_index]
        points[pivot_index] = points[right]
        points[right] = temp

        store_index = left
        for i in range(left, right):
            if squared_distance(points[i]) < pivot_dist:
                temp2 = points[store_index]
                points[store_index] = points[i]
                points[i] = temp2
                store_index = store_index + 1

        temp3 = points[store_index]
        points[store_index] = points[right]
        points[right] = temp3

        return store_index

    def quickselect(left, right, k_smallest):
        while left < right:
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == k_smallest:
                break

            if pivot_index < k_smallest:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    quickselect(0, len(points) - 1, k)
    result = points[:k]
    return result

print(kClosestPoints([[1,3],[-2,2]],1))