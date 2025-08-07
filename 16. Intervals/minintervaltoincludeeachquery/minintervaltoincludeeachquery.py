# leetcode 1851
# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti
# and ending at righti (inclusive).
# The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i
# such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Time Complexity:
# Space Complexity:
from typing import List
import heapq
from heapq import heappush, heappop
def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    # prepare answers, default to -1
    answer = [-1] * len(queries)

    # sort intervals by start time
    intervals.sort()

    # get query indices in ascending order of query value
    query_order = list(range(len(queries)))
    query_order.sort(key=lambda i: queries[i])

    ptr = 0          # where we are in the intervals list
    heap = []        # min-heap of (size, start, end)

    for qi in query_order:
        q = queries[qi]

        # drop any intervals that end before q
        while heap and heap[0][2] < q:
            heappop(heap)

        # add all intervals that start on or before q
        while ptr < len(intervals) and intervals[ptr][0] <= q:
            start, end = intervals[ptr]
            if end >= q:
                size = end - start + 1
                heappush(heap, (size, start, end))
            ptr += 1

        # the top of the heap is the smallest interval covering q
        if heap:
            answer[qi] = heap[0][0]

    return answer