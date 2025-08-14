# leetcode 200
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
from collections import deque

# Time Complexity: O(R x C)
# Space Complexity: O(1)
from typing import List

def numIslands(self, grid: List[List[str]]) -> int:
    # If the grid is empty or has no columns, there are no islands
    if not grid or not grid[0]:
        return 0

    # Save row and column counts so we don't recompute them
    rows = len(grid)
    cols = len(grid[0])

    # This will count how many separate islands we find
    islands = 0

    # Look at every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we see land ('1'), we've found a new island
            if grid[r][c] == '1':
                islands += 1                 # count this island
                stack = [(r, c)]             # start a DFS stack from this cell
                grid[r][c] = '0'             # mark it visited by turning it into water

                # Flood-fill: keep exploring until this island is fully marked
                while stack:
                    cr, cc = stack.pop()     # take one cell to explore its neighbors

                    # Check the neighbor above (if in bounds and is land)
                    if cr > 0 and grid[cr - 1][cc] == '1':
                        grid[cr - 1][cc] = '0'       # mark visited
                        stack.append((cr - 1, cc))   # explore it later

                    # Check the neighbor below
                    if cr + 1 < rows and grid[cr + 1][cc] == '1':
                        grid[cr + 1][cc] = '0'
                        stack.append((cr + 1, cc))

                    # Check the neighbor to the left
                    if cc > 0 and grid[cr][cc - 1] == '1':
                        grid[cr][cc - 1] = '0'
                        stack.append((cr, cc - 1))

                    # Check the neighbor to the right
                    if cc + 1 < cols and grid[cr][cc + 1] == '1':
                        grid[cr][cc + 1] = '0'
                        stack.append((cr, cc + 1))

    # After scanning the whole grid, 'islands' holds the total count
    return islands

print(numberOfIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))