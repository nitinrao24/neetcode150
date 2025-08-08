# leetcode 287
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

def find_duplicate(nums: List[int]) -> int:
    """Find the duplicate number in an array."""
    # Treat the array as a linked list:
    # - Each index is a node
    # - The "next" pointer is nums[index]
    # Because one number repeats, two indices point to the same next node,
    # creating a cycle whose entry point is the duplicate value.

    # Phase 1: Find the meeting point inside the cycle
    slow = nums[0]           # moves one step at a time
    fast = nums[0]           # moves two steps at a time
    while True:
        slow = nums[slow]          # 1-step move
        fast = nums[nums[fast]]    # 2-step move
        if slow == fast:           # pointers meet inside the cycle
            break

    # Phase 2: Find the entry to the cycle (the duplicate number)
    finder = nums[0]         # start a new pointer from the head
    while finder != slow:    # move both one step until they meet at cycle start
        finder = nums[finder]
        slow = nums[slow]

    return finder


