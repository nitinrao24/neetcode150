# leetcode 19
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional
# Time Complexity:
# Space Complexity:

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        slow = sentinel
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return sentinel.next