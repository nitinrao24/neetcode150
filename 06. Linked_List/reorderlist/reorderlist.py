# leetcode 143
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
from typing import Optional
# Time Complexity: O(n)
# Space Complexity: O(1)
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorder list as: L0 → Ln → L1 → Ln-1 → …."""
        # Find the midpoint of the list
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Split off and reverse the second half
        second = slow.next
        slow.next = None  # Terminate first half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge the two halves, alternating nodes
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

