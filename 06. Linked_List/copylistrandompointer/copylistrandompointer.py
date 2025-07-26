# leetcode 138
# A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.
# Construct a deep copy of the list.
# The deep copy should consist of exactly n brand new nodes,
# where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
# the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.
from typing import Optional
# Time Complexity:
# Space Complexity:


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        current = head

        while current:
            new_node = Node(current.val)
            node_map[current] = new_node
            current = current.next

        current = head

        while current:
            new_node = node_map[current]
            new_node.next = node_map[current.next]
            new_node.random = node_map[current.random]
            current = current.next

        return node_map[head]

