# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

# Time Complexity:
# Space Complexity:
from typing import List
from collections import deque
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # A tree with n nodes must have exactly n-1 edges
    if len(edges) > n - 1:
        return False

    # Build adjacency list for each node
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Track visited nodes and initialize BFS queue with node 0 (no parent)
    visited = set([0])
    queue = deque([(0, -1)])  # (current_node, parent_node)

    # Perform BFS to detect cycles and check connectivity
    while queue:
        current, parent = queue.popleft()
        for nbr in graph[current]:
            # Skip the edge back to parent
            if nbr == parent:
                continue
            # If we revisit a node, there's a cycle
            if nbr in visited:
                return False
            visited.add(nbr)
            queue.append((nbr, current))

    # All nodes must be reached for the graph to be connected
    return len(visited) == n