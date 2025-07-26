# leetcode 347
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
import heapq
from collections import defaultdict
from typing import List
# Time Complexity: O(n+k)
# Space Complexity: O(n)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 1) Build a frequency map and track the maximum count seen
    freq = {}  # map from number → its count
    max_count = 0  # highest frequency we’ve encountered
    for x in nums:
        # increase the count for x (default 0 → 1, etc.)
        freq[x] = freq.get(x, 0) + 1
        # update our record of the largest count
        if freq[x] > max_count:
            max_count = freq[x]

    # 2) Make buckets: an array of lists, index = frequency
    #    We only need indices 0 … max_count
    buckets: List[List[int]] = [[] for _ in range(max_count + 1)]

    # 3) Place each number into the bucket matching its frequency
    for num, count in freq.items():
        buckets[count].append(num)

    # 4) Collect the top k by scanning from highest freq → lowest
    result: List[int] = []
    for count in range(max_count, 0, -1):  # skip bucket[0], no-appearance
        for num in buckets[count]:  # all nums with this freq
            result.append(num)  # add it to our answer
            if len(result) == k:  # once we have k, stop
                return result

    return result  # (in case k == 0)

def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
    # 1) Count how many times each number appears
    freq = {}  # Create an empty map
    for num in nums:
        freq[num] = freq.get(num, 0) + 1  # Increase count for this num

    # 2) Use a min-heap of size at most k to track the k biggest frequencies
    heap = []  # Start with an empty heap
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))  # Push a (frequency, value) pair
        if len(heap) > k:  # If we have more than k items,
            heapq.heappop(heap)  # pop the smallest-frequency one

    # 3) Extract the numbers from the heap
    top_k = []
    while heap:  # Heap has up to k items
        count, num = heapq.heappop(heap)  # Pop smallest-frequency first
        top_k.append(num)  # Save the number

    return top_k[::-1]  # Reverse to go from highest to lowest

def topkfreqelements2(nums,k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    buckets = []
    for _ in range(len(nums) + 1):
        buckets.append([])

    for num, count in frequency_map.items():
        buckets[count].append(num)

    top_k = []
    for size in range(len(buckets) - 1, -1, -1):
        group = buckets[size]
        for num in group:
            top_k.append(num)
            if len(top_k) == k:
                return top_k

print(topKFrequent([1,1,1,2,2,3],2))