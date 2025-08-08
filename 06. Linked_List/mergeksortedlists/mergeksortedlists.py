# leetcode 23
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Time Complexity: mergeKLists: O(N log k) where N is the total number of nodes across all lists and k is the number of lists (pairwise merging halves the number of lists each round).merge_lists (two lists): O(n₁ + n₂).
# Space Complexity: O(1) auxiliary pointer space for merging nodes in place.
# O(k) for temporary arrays of list references during rounds (no extra node allocations).
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, list_nodes: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists into a single sorted linked list."""
        # If there are no lists, the result is empty
        if not list_nodes:
            return None

        # Repeatedly merge lists in pairs until only one list remains
        while len(list_nodes) > 1:
            merged_lists: List[Optional[ListNode]] = []

            # Take lists two at a time: (0,1), (2,3), ...
            for i in range(0, len(list_nodes), 2):
                first = list_nodes[i]
                # If there's an odd one out, pair it with None (no-op merge)
                second = list_nodes[i + 1] if i + 1 < len(list_nodes) else None

                # Merge this pair and collect the result
                merged_pair = self.merge_lists(first, second)
                merged_lists.append(merged_pair)

            # The merged results become the new round's inputs
            list_nodes = merged_lists

        # Only one list left: that's the fully merged list
        return list_nodes[0]

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists into a single sorted linked list."""
        # Dummy head to simplify pointer manipulation
        sentinel = ListNode()
        tail = sentinel

        # Walk both lists and pick the smaller head each time
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Advance the tail as we extend the merged list
            tail = tail.next

        # Attach whatever remains from either list
        tail.next = list1 if list1 else list2

        # Skip the dummy and return the real head
        return sentinel.next