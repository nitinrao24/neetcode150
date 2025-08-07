# leetcode 2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
from typing import Optional
# Definition for singly-linked list.
# Time Complexity: O(max(len(l1), len(l2)))
# Space Complexity: O(max(len(l1), len(l2)))
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy start node to simplify list construction
        sentinel = ListNode()
        # 'tail' will always point to the last node in our result list
        tail = sentinel
        # 'carry' holds any overflow from summing two digits (0 or 1)
        carry = 0

        # Continue as long as either list has digits left or there’s a carry
        while l1 or l2 or carry:
            # Start this digit’s total with whatever carry we brought forward
            total = carry

            # If l1 still has a digit, add it and advance l1
            if l1:
                total += l1.val
                l1 = l1.next

            # Likewise for l2
            if l2:
                total += l2.val
                l2 = l2.next

            # The digit to store here is total mod 10
            digit = total % 10
            # Update carry for the next round (either 0 or 1)
            carry = total // 10

            # Append a new node with this digit to our result list
            tail.next = ListNode(digit)
            tail = tail.next  # Move tail to point at the new last node

        # The real result starts at sentinel.next (skipping the dummy)
        return sentinel.next



    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        tail = sentinel
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

        return sentinel.next