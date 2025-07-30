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
        # Create an empty list to hold all pushed values
        self.stack = []
        # Create a second empty list to track the current minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        # 1) Always push the new value onto the main stack
        self.stack.append(val)
        # 2) If min_stack is empty OR the new value is <= the current minimum,
        #    push it onto min_stack so it becomes the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 1) Pop the top value off the main stack
        val = self.stack.pop()
        # 2) If that value was the current minimum, pop it from min_stack too
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top of the main stack (most recently pushed value),
        # or None if the stack is empty
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top of min_stack (current minimum),
        # or None if no values have been pushed
        return self.min_stack[-1] if self.min_stack else None

class MinStack1:

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

