# leetcode 141
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def linkedListCycle(head):
        """Detect if linked list has a cycle."""
        # 'slow' moves one step at a time, 'fast' moves two steps
        slow = head
        fast = head

        # Traverse until fast reaches the end or pointers meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, a cycle exists
            if slow == fast:
                return True

        # Fast reached the end—no cycle
        return False