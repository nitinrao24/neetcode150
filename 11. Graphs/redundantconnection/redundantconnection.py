# leetcode 684
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

# Time Complexity:
# Space Complexity:
from typing import List
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # Start with each node as its own parent
    parent = list(range(len(edges) + 1))

    def find_parent(x: int) -> int:
        # Climb up until we find the top parent
        if parent[x] != x:
            parent[x] = find_parent(parent[x])  # flatten the path
        return parent[x]

    # Try adding each edge
    for u, v in edges:
        pu = find_parent(u)
        pv = find_parent(v)

        # If u and v share the same top parent, this edge creates a cycle
        if pu == pv:
            return [u, v]

        # Otherwise, link v's group to u's group
        parent[pv] = pu

    # No cycle found
    return []