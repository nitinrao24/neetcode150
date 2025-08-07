# leetcode 19
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Remove the n-th node from the end of the list."""
        # Create a sentinel node that simplifies removal, even at the head
        sentinel = ListNode(0, head)
        # 'slow' will end up just before the node we want to remove
        slow = sentinel
        # 'fast' will be used to find the end of the list
        fast = head

        # Advance 'fast' by n steps
        for _ in range(n):
            fast = fast.next

        # Move both pointers until 'fast' reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # 'slow.next' is the node to remove—skip it
        slow.next = slow.next.next

        # Return the (possibly new) head of the list
        return sentinel.next