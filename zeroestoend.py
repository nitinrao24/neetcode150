# move all zeroes in a given input array to the end
# leetcode 283
def moveZeroes(inputarray):
    for i in range(0,len(inputarray)):
        if inputarray[i] == 0:
            inputarray.append(inputarray[i])
            inputarray.remove(inputarray[i])
    return inputarray

input = [1,0,0,2,3,0,0,2]
outputarray = moveZeroes(input)
print(outputarray)