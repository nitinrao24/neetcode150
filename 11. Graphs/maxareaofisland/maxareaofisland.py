# leetcode 695
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Time Complexity:
# Space Complexity:

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited_cells = set()
    max_area = 0

    def dfs(r, c):
        if r not in range(rows) or c not in range(cols) or (r, c) in visited_cells or grid[r][c] == 0:
            return 0

        visited_cells.add((r, c))

        up_area = dfs(r - 1, c)
        down_area = dfs(r + 1, c)
        left_area = dfs(r, c - 1)
        right_area = dfs(r, c + 1)

        return 1 + up_area + down_area + left_area + right_area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited_cells:
                area = dfs(r, c)
                if area > max_area:
                    max_area = area

    return max_area

print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))