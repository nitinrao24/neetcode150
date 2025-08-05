# leetcode 678
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# Time Complexity:
# Space Complexity:

def validParanthesis(s):
    min_open = 0
    max_open = 0

    for char in s:
        if char == "(":
            min_open += 1
            max_open += 1
        elif char == ")":
            min_open -= 1
            max_open -= 1
        else:
            # wildcard can be '(' or ')' or empty
            min_open -= 1
            max_open += 1

        if max_open < 0:
            return False

        if min_open < 0:
            min_open = 0

    return min_open == 0