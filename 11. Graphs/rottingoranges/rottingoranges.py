# leetcode 994
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

# Time Complexity:
# Space Complexity:
from collections import deque
def rottingOranges(grid):
    num_rows = len(grid)
    if num_rows == 0:
        return -1

    num_cols = len(grid[0])

    fresh_count = 0
    queue = deque()

    # initialize with all currently rotten oranges and count fresh ones
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh_count += 1

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # BFS by layers: each layer is one minute
    while queue and fresh_count > 0:
        minutes += 1
        layer_size = len(queue)

        for _ in range(layer_size):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # skip out-of-bounds
                if not (0 <= nr < num_rows and 0 <= nc < num_cols):
                    continue

                # skip empty or already rotten
                if grid[nr][nc] != 1:
                    continue

                # rot this fresh orange
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc))

    # if any fresh left, impossible
    if fresh_count > 0:
        return -1

    return minutes