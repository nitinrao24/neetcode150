# leetcode 25
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Time Complexity:
# Space Complexity:
from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        group_tail = head

        for _ in range(k):
            if group_tail is None:
                return head
            group_tail = group_tail.next

        def reverse_segment(start_node, end_node):
            previous_node = None
            current_node = start_node

            while current_node is not end_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            return previous_node

        reversed_head = reverse_segment(head, group_tail)

        head.next = self.reverseKGroup(group_tail, k)

        return reversed_head