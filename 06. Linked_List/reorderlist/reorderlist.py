# leetcode 143
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
from typing import Optional
# Time Complexity:
# Space Complexity:
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        second_half = slow_ptr.next
        slow_ptr.next = None

        prev_node = None

        while second_half:
            next_temp = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_temp

        first_half = head
        second_half = prev_node

        while second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next

