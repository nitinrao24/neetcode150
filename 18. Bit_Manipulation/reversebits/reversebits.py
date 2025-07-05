# reverses an array of characters
# leetcode 344
def reverseString(inputarray):
    startindex = 0
    endindex = len(inputarray)-1
    while startindex < endindex:
        temp = inputarray[startindex]
        inputarray[startindex] = inputarray[endindex]
        inputarray[endindex] = temp
        startindex += 1
        endindex -= 1
    return inputarray

input = ["H", "a", "n", "n", "a", "h"]
outputarray = reverseString(input)
print(outputarray)
