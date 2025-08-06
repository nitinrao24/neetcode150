# leetcode 206
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse a singly linked list."""
        # 'prev' will trail behind 'curr' and become the new head at the end
        prev: Optional[ListNode] = None
        # 'curr' starts at the head of the original list
        curr: Optional[ListNode] = head

        # Iterate until we've processed every node
        while curr is not None:
            # Temporarily store the next node
            next_temp: Optional[ListNode] = curr.next
            # Reverse the 'next' pointer of the current node
            curr.next = prev
            # Move 'prev' and 'curr' one step forward
            prev = curr
            curr = next_temp

        return prev

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(reverseLinkedList(n1))
print(n2)