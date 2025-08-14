# leetcode 51
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Time Complexity:
# Space Complexity:
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r - c ) in diag1 or (r+c) in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r+c)
                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
        backtrack(0)
        return res