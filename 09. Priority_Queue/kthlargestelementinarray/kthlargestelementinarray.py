# leetcode 215
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Time Complexity:
# Space Complexity:

import heapq

def kthLargest(nums,k):
    heap = []

    for value in nums:
        heapq.heappush(heap, value)

        size = len(heap)
        if size > k:
            heapq.heappop(heap)

    result = heap[0]
    return result

print(kthLargest([3,2,1,5,6,4],2))
