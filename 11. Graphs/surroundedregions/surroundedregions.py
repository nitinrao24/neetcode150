# leetcode 130
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board.
# You do not need to return anything.

# Time Complexity:
# Space Complexity:
from collections import deque
def surroundedregions(board):
    # character that should not be flipped if connected to border
    o_char = "O"

    # dimensions
    rows = len(board)
    cols = len(board[0])

    # BFS queue for border-connected O's
    queue = deque()

    # enqueue O's on left and right borders
    for r in range(rows):
        if board[r][0] == o_char:
            queue.append((r, 0))
        if board[r][cols - 1] == o_char:
            queue.append((r, cols - 1))

    # enqueue O's on top and bottom borders
    for c in range(cols):
        if board[0][c] == o_char:
            queue.append((0, c))
        if board[rows - 1][c] == o_char:
            queue.append((rows - 1, c))

    def is_in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # mark all O's reachable from the border with a temporary marker #
    while queue:
        r, c = queue.popleft()
        board[r][c] = "#"

        # explore four directions
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc

            if not is_in_bounds(nr, nc):
                continue

            if board[nr][nc] != o_char:
                continue

            queue.append((nr, nc))
            board[nr][nc] = "#"

    # flip interior O's to X and restore border-connected ones
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == o_char:
                board[r][c] = "X"
            elif board[r][c] == "#":
                board[r][c] = o_char