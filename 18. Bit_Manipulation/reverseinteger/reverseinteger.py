# leetcode 7
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Time Complexity:
# Space Complexity:

def reverseInteger(num):
    result = 0
    if num < 0:
        result = int(str(num)[1:][::-1]) * -1
    else:
        result = int(str(num)[::-1])

    if result > 2 ** 31 - 1 or result < -2 ** 31:
        return 0

    return result

print(reverseInteger(123))
print(reverseInteger(-123))
print(reverseInteger(120))