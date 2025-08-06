# leetcode 1584
# Return the minimum cost to make all points connected.
# All points are connected if there is exactly one simple path between any two points.

# Time Complexity:
# Space Complexity:
from typing import List
import heapq
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # how many points we have
    count = len(points)

    # total cost to connect all points
    total = 0

    # mark which points we've already connected
    seen = [False] * count

    # min-heap to pick the next cheapest connection: (cost, point_index)
    heap = [(0, 0)]

    # best[p] = cheapest cost we've seen so far to connect point p
    best = {0: 0}

    # keep going until we've connected all points
    while heap:
        cost, curr = heapq.heappop(heap)

        # if it's already connected, skip it
        if seen[curr]:
            continue

        # connect this point and add its cost
        seen[curr] = True
        total += cost

        # try linking every other unconnected point
        for nxt in range(count):
            if not seen[nxt]:
                # Manhattan distance between curr and nxt
                d = abs(points[curr][0] - points[nxt][0]) \
                    + abs(points[curr][1] - points[nxt][1])

                # if this path is cheaper, remember it and push to heap
                if d < best.get(nxt, float('inf')):
                    best[nxt] = d
                    heapq.heappush(heap, (d, nxt))

    return total