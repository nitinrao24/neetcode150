# leetcode 25
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Time Complexity: O(n) — each node is visited a constant number of times
# Space Complexity: O(n/k) due to recursion depth (worst-case O(n) if k == 1)
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse the linked list in groups of k nodes (recursively)."""
        if head is None:
            return None  # Empty list stays empty

        # Move a pointer k steps ahead to check if a full group exists.
        # If we run out of nodes before k steps, we don't reverse this partial group.
        group_tail = head
        for _ in range(k):
            if group_tail is None:
                return head  # Not enough nodes for a full group
            group_tail = group_tail.next  # 'group_tail' is the node *after* the k-group

        # Helper: reverse the list from start_node up to but *not* including end_node.
        def reverse_segment(start_node: Optional[ListNode],
                            end_node: Optional[ListNode]) -> Optional[ListNode]:
            prev_node = None
            curr = start_node
            # Reverse pointers until we reach the exclusive end
            while curr is not end_node:
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node
            # 'prev_node' is the new head of the reversed segment
            return prev_node

        # Reverse the first k nodes. 'reversed_head' becomes the new head of this segment.
        reversed_head = reverse_segment(head, group_tail)

        # 'head' is now the tail of the reversed segment.
        # Recursively process the remaining list starting at 'group_tail'
        # and connect it after the current reversed segment.
        head.next = self.reverseKGroup(group_tail, k)

        # Return the head of the reversed segment
        return reversed_head