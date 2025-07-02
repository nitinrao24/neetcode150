# leetcode 1480
# trying to sum all elements of list
def runningSum(inputarr):
    outputarray = []
    total = 0
    for i in range (0,len(inputarr)):
        total += inputarr[i]
        outputarray.insert(i,total)
    return outputarray
def runningSum2(inputarr):
    outputarray = [0] * len(inputarr)
    outputarray[0] = inputarr[0]
    for i in range (1,len(inputarr)):
        outputarray[i] = outputarray[i-1] + inputarr[i]
    return outputarray


inputarr = [1,2,3,4]
arr2 = [1,1,1,1,1]
arr3 = [3,1,2,10,1]
print(arr3)
print(runningSum2(arr3))