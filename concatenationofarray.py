# leetcode 1929
# concatenating the array twice
def getConcatenation(inputarray):
    outputarray = [0]*2*len(inputarray)
    for i in range(0,len(inputarray)):
        outputarray[i] = inputarray[i]
    for i in range(len(inputarray), 2*len(inputarray)):
        outputarray[i] = inputarray[i - len(inputarray)]
    return outputarray

arr1 = [1,2,1]
arr2 = [1,3,2,1]
outputarray = getConcatenation(arr2)
print(arr2)
print(outputarray)