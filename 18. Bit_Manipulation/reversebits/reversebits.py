# Leetcode 190
# Reverse bits of a given 32 bits unsigned integer.

# Time Complexity:
# Space Complexity:
def reverseBits(binarynumber):
    bits = binarynumber[::-1]
    return int(bits, 2)

print(reverseBits("00000010100101000001111010011100"))
print(reverseBits("11111111111111111111111111111101"))