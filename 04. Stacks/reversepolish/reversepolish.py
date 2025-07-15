# leetcode 150
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# Time Complexity:
# Space Complexity:

def reversePolish(tokens):
    values = []

    for token in tokens:
        if token == "+":
            right_operand = values.pop()
            left_operand = values.pop()
            values.append(left_operand + right_operand)

        elif token == "-":
            right_operand = values.pop()
            left_operand = values.pop()
            values.append(left_operand - right_operand)

        elif token == "*":
            right_operand = values.pop()
            left_operand = values.pop()
            values.append(left_operand * right_operand)

        elif token == "/":
            right_operand = values.pop()
            left_operand = values.pop()
            values.append(int(left_operand / right_operand))

        else:
            values.append(int(token))

    return values[0]

print(reversePolish(["2","1","+","3","*"]))
print(reversePolish(["4","13","5","/","+"]))