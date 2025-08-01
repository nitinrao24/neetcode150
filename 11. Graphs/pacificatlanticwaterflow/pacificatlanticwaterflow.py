# leetcode 417
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells.
# You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level
# of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
# if the neighboring cell's height is less than or equal to the current cell's height.
# Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
# can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Time Complexity:
# Space Complexity:
from collections import deque
def pacificatlanticwaterflow(heights):
    # if input is empty, nothing to do
    if not heights:
        return []

    # dimensions
    rows = len(heights)
    cols = len(heights[0])

    # reachability grids for Pacific and Atlantic
    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]

    # directions: left, right, up, down
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def bfs(start_row, start_col, visited):
        queue = deque()
        queue.append((start_row, start_col))
        visited[start_row][start_col] = True

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # bounds check
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                # already visited skip
                if visited[new_row][new_col]:
                    continue

                # can only flow from lower/equal to higher (reverse BFS)
                if heights[row][col] <= heights[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

    # start BFS from Pacific edges (top row and left column)
    for r in range(rows):
        bfs(r, 0, pacific_reachable)
    for c in range(cols):
        bfs(0, c, pacific_reachable)

    # start BFS from Atlantic edges (bottom row and right column)
    for r in range(rows):
        bfs(r, cols - 1, atlantic_reachable)
    for c in range(cols):
        bfs(rows - 1, c, atlantic_reachable)

    # collect cells reachable by both oceans
    result = []
    for r in range(rows):
        for c in range(cols):
            if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                result.append([r, c])

    return result