# leetcode 329
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down.
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Time Complexity:
# Space Complexity:
from typing import List
class Solution:
    def dfs(self, matrix: List[List[int]], row: int, col: int, memo: List[List[int]]) -> int:
        """
        Returns the length of the longest strictly increasing path
        starting from cell (row, col) in the matrix.
        Uses memoization to avoid recomputing cells.
        """
        # If we've already computed this cell, just return it
        if memo[row][col]:
            return memo[row][col]

        # Get number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Possible directions: right, left, up, down
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Track the best length from this cell
        max_len = 0

        # Explore each neighbor
        for dr, dc in dirs:
            next_row = row + dr
            next_col = col + dc

            # Check bounds and increasing condition
            if (0 <= next_row < rows and
                    0 <= next_col < cols and
                    matrix[next_row][next_col] > matrix[row][col]):

                # Recursively explore neighbor
                path_len = self.dfs(matrix, next_row, next_col, memo)
                if path_len > max_len:
                    max_len = path_len

        # Include this cell in the count (+1)
        memo[row][col] = 1 + max_len
        return memo[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Computes the overall longest increasing path in the entire matrix.
        Initializes a memo table and runs DFS from every cell.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # memo[row][col] will hold the LIS starting at (row, col)
        memo = [[0] * cols for _ in range(rows)]

        # Compute the DFS for every cell and take the maximum
        best = 0
        for r in range(rows):
            for c in range(cols):
                current = self.dfs(matrix, r, c, memo)
                if current > best:
                    best = current

        return best

