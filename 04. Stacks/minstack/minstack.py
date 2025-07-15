# leetcode 155
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Time Complexity:
# Space Complexity:

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min is None or val < current_min:
            current_min = val

        node = [val, current_min]
        self.st.append(node)

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if not self.st:
            return None

        top_node = self.st[-1]
        return top_node[0]

    def getMin(self) -> int:
        if not self.st:
            return None

        top_node = self.st[-1]
        return top_node[1]

