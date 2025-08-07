# leetcode 743
# You are given a network of n nodes, labeled from 1 to n. You are also given times,
# a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
# vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k.
# Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

# Time Complexity:
# Space Complexity:
import heapq
from typing import List
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # build a graph: each node maps to a list of (neighbor, travel_time)
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    # set up distances: start with “infinity” for everyone except the start node
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0

    # min-heap to grab the next node with the smallest known distance
    heap = [(0, k)]

    while heap:
        curr_time, node = heapq.heappop(heap)

        # if we’ve already found a quicker way to this node, skip it
        if curr_time > dist[node]:
            continue

        # otherwise, look at each neighbor and see if we can improve its time
        for nei, w in graph[node]:
            new_time = curr_time + w
            if new_time < dist[nei]:
                dist[nei] = new_time
                heapq.heappush(heap, (new_time, nei))

    # after Dijkstra, the answer is the max distance to any node
    max_delay = max(dist.values())
    if max_delay == float('inf'):
        # some node wasn’t reachable
        return -1

    return max_delay