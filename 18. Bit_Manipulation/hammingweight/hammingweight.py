# leetcode 191
# Given a positive integer n,
# write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Time Complexity:
# Space Complexity:
def hammingWeight(num):
    count = 0
    binum = bin(num)[2:]
    for i in binum:
        if i == '1':
            count += 1
    return count

print(hammingWeight(2147483645))
