# leetcode 787
# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei] indicates
# that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.

# Time Complexity:
# Space Complexity:
from typing import List
import heapq
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # make a graph: city -> list of (next_city, price)
    graph = {i: [] for i in range(n)}
    for u, v, price in flights:
        graph[u].append((v, price))

    # best_cost[i] is the cheapest price we've seen to reach city i
    best_cost = [float('inf')] * n
    best_cost[src] = 0

    # heap entries are (stops_used, current_city, total_cost)
    heap = []
    heapq.heappush(heap, (0, src, 0))

    # explore while we have possible routes
    while heap:
        stops, city, cost = heapq.heappop(heap)

        # if we've already used too many stops, skip this route
        if stops > k:
            continue

        # look at all flights out of this city
        for neighbor, price in graph[city]:
            new_cost = cost + price

            # if this route is cheaper, remember it and keep exploring
            if new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                heapq.heappush(heap, (stops + 1, neighbor, new_cost))

    # if destination never got updated, it's unreachable
    if best_cost[dst] == float('inf'):
        return -1

    return best_cost[dst]