# leetcode 338
# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Time Complexity:
# Space Complexity:
def countBits(n):
    newArray = [0]*(n+1)
    for i in range(0, n+1):
        count = 0
        intversion = bin(i)[2:]
        for j in intversion:
            count += int(j)
        newArray[i] = count
    return newArray

print(countBits(2))
print(countBits(5))
