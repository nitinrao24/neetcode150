# leetcode 133
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Time Complexity:
# Space Complexity:


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        queue = deque([node])
        node_to_clone = {node: Node(node.val, [])}

        while queue:
            original = queue.popleft()
            clone = node_to_clone[original]

            for neighbor in original.neighbors:
                if neighbor not in node_to_clone:
                    neighbor_clone = Node(neighbor.val, [])
                    node_to_clone[neighbor] = neighbor_clone
                    queue.append(neighbor)
                clone.neighbors.append(node_to_clone[neighbor])

        return node_to_clone[node]