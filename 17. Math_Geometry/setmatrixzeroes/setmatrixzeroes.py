# leetcode 73
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

def setMatrixZeroes(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row_zero = False
    col_zero = False
    for col in range(num_cols):
        if matrix[0][col] == 0:
            row_zero = True
            break
    for row in range(num_rows):
        if matrix[row][0] == 0:
            col_zero = True
            break
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
    for row in range(1, num_rows):
        if matrix[row][0] == 0:
            for col in range(1, num_cols):
                matrix[row][col] = 0
    for col in range(1, num_cols):
        if matrix[0][col] == 0:
            for row in range(1, num_rows):
                matrix[row][col] = 0
    if row_zero:
        for col in range(num_cols):
            matrix[0][col] = 0
    if col_zero:
        for row in range(num_rows):
            matrix[row][0] = 0
    return matrix

print(setMatrixZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))