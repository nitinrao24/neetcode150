# leetcode 347
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Time Complexity:
# Space Complexity:

def topkfreqelements(nums,k):
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

print(topkfreqelements([1,1,1,2,2,3],2))