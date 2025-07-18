# leetcode 74
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# Time Complexity:
# Space Complexity:

def search2DMatrix(matrix, target):
    row_start = 0
    row_end = len(matrix) - 1

    while row_start <= row_end:
        row_mid = (row_start + row_end) // 2
        first_in_row = matrix[row_mid][0]
        last_in_row = matrix[row_mid][-1]

        if first_in_row <= target <= last_in_row:
            break
        elif first_in_row > target:
            row_end = row_mid - 1
        else:
            row_start = row_mid + 1

    row = (row_start + row_end) // 2

    col_start = 0
    col_end = len(matrix[row]) - 1

    while col_start <= col_end:
        col_mid = (col_start + col_end) // 2
        current_value = matrix[row][col_mid]

        if current_value == target:
            return True
        elif current_value > target:
            col_end = col_mid - 1
        else:
            col_start = col_mid + 1

    return False

print(search2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
