# There is an undirected graph with n nodes.
# There is also an edges array, where edges[i] = [a, b]
# means that there is an edge between node a and node b in the graph.
# The nodes are numbered from 0 to n - 1.
# Return the total number of connected components in that graph.

# Time Complexity:
# Space Complexity:
from typing import List
from collections import deque
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # Build adjacency list for the undirected graph
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    # Track which nodes have been visited
    visited = [False] * n

    def bfs(start: int) -> None:
        """
        Perform breadth-first search from the start node,
        marking all reachable nodes as visited.
        """
        queue = deque([start])
        visited[start] = True

        while queue:
            current = queue.popleft()
            for neighbor in neighbors[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    # Count how many connected components exist
    component_count = 0
    for node in range(n):
        if not visited[node]:
            bfs(node)
            component_count += 1

    return component_count