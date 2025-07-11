# leetcode 36
# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Time Complexity:
# Space Complexity:

from collections import defaultdict
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen_rows = defaultdict(set)
    seen_columns = defaultdict(set)
    seen_blocks = defaultdict(set)
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                continue
            block_key = (r // 3, c // 3)
            if (value in seen_rows[r] or value in seen_columns[c] or value in seen_blocks[block_key]):
                return False
            seen_rows[r].add(value)
            seen_columns[c].add(value)
            seen_blocks[block_key].add(value)
    return True