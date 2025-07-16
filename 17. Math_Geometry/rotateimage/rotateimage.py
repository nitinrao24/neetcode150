# leetcode 58
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

def rotateImage(matrix):
    size = len(matrix)
    top_row = 0
    bottom_row = size - 1

    while top_row < bottom_row:
        for col_idx in range(size):
            temp_value = matrix[top_row][col_idx]
            matrix[top_row][col_idx] = matrix[bottom_row][col_idx]
            matrix[bottom_row][col_idx] = temp_value

        top_row += 1
        bottom_row -= 1

    for row_idx in range(size):
        for col_idx in range(row_idx + 1, size):
            temp_value = matrix[row_idx][col_idx]
            matrix[row_idx][col_idx] = matrix[col_idx][row_idx]
            matrix[col_idx][row_idx] = temp_value

    return matrix

print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))