# leetcode 286
# You are given a m×n 2D grid initialized with these three possible values:
# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest.
# If a land cell cannot reach a treasure chest then the value should remain INF.

# Time Complexity:
# Space Complexity:
from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row_count = len(grid)  # number of rows in the grid
        col_count = len(grid[0])  # number of columns in the grid
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # four cardinal directions
        INF = 2147483647  # sentinel for unreachable

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))  # begin from the INF cell
            visited = [[False for _ in range(col_count)] for _ in range(row_count)]
            visited[start_row][start_col] = True  # mark starting cell as seen
            distance = 0  # current distance from this cell to nearest gate

            while queue:
                level_size = len(queue)  # number of nodes at current distance
                for _ in range(level_size):
                    row, col = queue.popleft()

                    if grid[row][col] == 0:  # found a gate
                        return distance

                    for dr, dc in moves:
                        new_row = row + dr
                        new_col = col + dc

                        if 0 <= new_row < row_count and 0 <= new_col < col_count:
                            if not visited[new_row][new_col] and grid[new_row][new_col] != -1:
                                visited[new_row][new_col] = True
                                queue.append((new_row, new_col))

                distance += 1  # increment distance after exploring this layer

            return INF  # no gate reachable

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == INF:  # only run BFS from empty rooms
                    grid[r][c] = bfs(r, c)