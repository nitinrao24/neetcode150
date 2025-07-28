# leetcode 36
# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Create three lists of 9 zeros each to hold bitmasks for rows, columns, and 3×3 blocks
    row_mask = [0] * 9  # row_mask[r] uses 9 bits to track which numbers seen in row r
    col_mask = [0] * 9  # col_mask[c] does the same for column c
    block_mask = [0] * 9  # block_mask[b] for block b, with b = 0…8

    # Loop over every cell in the 9×9 board
    for r in range(9):
        for c in range(9):
            val = board[r][c]  # Read the character at row r, column c
            if val == ".":  # If it's an empty cell, skip the rest
                continue

            # Compute a bit corresponding to this digit ('1'→bit0, '2'→bit1, …, '9'→bit8)
            bit = 1 << (ord(val) - ord("1"))

            # Calculate which of the 9 blocks this cell is in:
            # block 0 covers rows 0–2 & cols 0–2,
            # block 1 covers rows 0–2 & cols 3–5, …, block 8 covers rows 6–8 & cols 6–8
            b = (r // 3) * 3 + (c // 3)

            # If that bit is already set in the row, column, or block mask, we have a duplicate
            if (row_mask[r] & bit) or \
                    (col_mask[c] & bit) or \
                    (block_mask[b] & bit):
                return False  # Duplicate found → invalid Sudoku

            # Otherwise, mark that number as seen by setting the bit in each mask
            row_mask[r] |= bit
            col_mask[c] |= bit
            block_mask[b] |= bit

    return True

def isValidSudoku1(self, board: List[List[str]]) -> bool:
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