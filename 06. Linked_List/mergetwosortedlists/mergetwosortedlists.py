# leetcode 21
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Time Complexity: O(len(list1) + len(list2))
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1,list2):
        """Merge two sorted linked lists."""
        # Create a dummy node to simplify edge cases
        dummy = ListNode(-1)
        # 'current' will build out the merged list
        current = dummy
        # Pointers for each input list
        p1, p2 = list1, list2

        # Traverse both lists until one is exhausted
        while p1 and p2:
            # Pick the smaller node to append next
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            # Advance the tail of the merged list
            current = current.next

        # Attach whichever list still has nodes remaining
        current.next = p1 if p1 else p2

        # The merged list starts after the dummy node
        return dummy.next
