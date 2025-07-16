# leetcode 54
# Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralMatrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    current_row = 0
    current_col = 0

    delta_row = 0
    delta_col = 1

    result = []
    total_cells = num_rows * num_cols

    while len(result) < total_cells:
        result.append(matrix[current_row][current_col])
        matrix[current_row][current_col] = "."

        next_row = current_row + delta_row
        next_col = current_col + delta_col

        if (not (0 <= next_row < num_rows)
                or not (0 <= next_col < num_cols)
                or matrix[next_row][next_col] == "."):
            temp = delta_col
            delta_col = -delta_row
            delta_row = temp

        current_row += delta_row
        current_col += delta_col

    return result

print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))
