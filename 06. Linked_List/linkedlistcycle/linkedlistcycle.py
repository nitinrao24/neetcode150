# leetcode 141
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Time Complexity:
# Space Complexity:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def linkedListCycle(head):
        n1 = head
        n2 = head

        while n1 and n1.next:
            n1 = n1.next.next
            n2 = n2.next

            if n1 == n2:
                return True

        return False