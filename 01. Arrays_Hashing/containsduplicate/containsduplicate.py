# returns true if duplicate element is found in array and returns false if elements are distinct
# leetcode 217
def containsDuplicate(inputarray):
    for i in range(0, len(inputarray)):
        for j in range(i + 1, len(inputarray)):
            if inputarray[i] == inputarray[j]:
                return True
    return False

input = [1,1,1,3,3,4,3,2,4,2]
outputarray = containsDuplicate(input)
print(outputarray)