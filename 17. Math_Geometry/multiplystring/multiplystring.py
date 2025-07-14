# leetcode 43
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Time Complexity:
# Space Complexity:

def multiplyString(num1,num2):
    value1 = 0
    value2 = 0
    for digit in num1:
        value1 = value1 * 10 + (ord(digit) - ord('0'))
    for digit in num2:
        value2 = value2 * 10 + (ord(digit) - ord('0'))
    return str(value1 * value2)

print(multiplyString("2","3"))