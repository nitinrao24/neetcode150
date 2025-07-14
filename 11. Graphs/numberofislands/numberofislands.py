# leetcode 200
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
from collections import deque

# Time Complexity:
# Space Complexity:
def numberOfIslands(grid):
    island_count = 0
    visited_cells = set()
    rows = len(grid)
    cols= len(grid[0])

    def bfs(r, c):
        queue = deque()
        visited_cells.add((r, c))
        queue.append((r, c))

        while queue:
            cell = queue.popleft()
            curr_row = cell[0]
            curr_col = cell[1]
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for row_offset, col_offset in neighbors:
                new_row = curr_row + row_offset
                new_col = curr_col + col_offset
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visited_cells):
                    queue.append((new_row, new_col))
                    visited_cells.add((new_row, new_col))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited_cells:
                island_count += 1
                bfs(r, c)

    return island_count

print(numberOfIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))