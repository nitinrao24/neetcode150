# leetcode 1470
# array is given in the format of x1 x2 ... y1 y2 ...
# given 2 parameters
# meant to return x1 y1 and x2 y2
def shuffleArray(arr, num):
    newArr = []
    for i in range(num):
        newArr.append(arr[i])
        newArr.append(arr[i+num])
    return newArr

arr1 = [0,2,1,5,3,4]
num1 = 3
outputarray = shuffleArray(arr1, num1)
print(outputarray)