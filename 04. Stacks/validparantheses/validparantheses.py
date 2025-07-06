# leetcode 20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Time Complexity:
# Space Complexity:

def isValidParantheses(inputstring):
    key = {')': '(', '}': '{', ']': '['}
    stack = []

    for i in inputstring:
        if i in key.values():
            stack.append(i)
        elif i in key:
            if not stack or stack.pop() != key[i]:
                return False
    return len(stack) == 0

print(isValidParantheses("()[]{}"))
print(isValidParantheses("(]"))