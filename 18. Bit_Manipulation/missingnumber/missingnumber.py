# leetcode 268
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Time Complexity:
# Space Complexity:
def missingNumber(inputarray):
    nset = set(inputarray)
    for i in range(0, len(inputarray)+1):
        if i not in nset:
            return i

print(missingNumber([9,6,4,2,3,5,7,0,1]))