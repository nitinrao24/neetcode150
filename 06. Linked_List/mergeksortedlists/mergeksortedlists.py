# leetcode 23
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
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
    def mergeKLists(self, list_nodes: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list_nodes:
            return None

        while len(list_nodes) > 1:
            merged_lists = []
            for idx in range(0, len(list_nodes), 2):
                first = list_nodes[idx]

                if idx + 1 < len(list_nodes):
                    second = list_nodes[idx + 1]
                else:
                    second = None

                merged_pair = self.merge_lists(first, second)
                merged_lists.append(merged_pair)

            list_nodes = merged_lists

        return list_nodes[0]

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        tail = sentinel

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return sentinel.next