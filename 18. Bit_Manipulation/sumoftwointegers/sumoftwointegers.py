# leetcode 371
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Time Complexity:
# Space Complexity:

def getSumOfTwoIntegers(a,b):
    mask = 0xFFFFFFFF
    while b:
        #Sum without carry: XOR of bits
        sum_no_carry = a ^ b

        #shifted left
        carry = (a & b) << 1

        # Apply the mask to simulate a 32 bit overflow
        a = sum_no_carry & mask
        b = carry & mask

    # If result is positive return it directly.
    if a <= 0x7FFFFFFF:
        return a
    else:
        return ~(a ^ mask)

print(getSumOfTwoIntegers(2,3))
print(getSumOfTwoIntegers(5,7))
print(getSumOfTwoIntegers(-8,-4))
print(getSumOfTwoIntegers(-5,7))