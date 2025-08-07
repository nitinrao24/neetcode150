# leetcode 778
# You are given an n x n integer matrix grid where each value grid[i][j]
# represents the elevation at that point (i, j).
# It starts raining, and water gradually rises over time.
# At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.
# You can swim from a square to another 4-directionally adjacent square if and only if
# the elevation of both squares individually are at most t.
# You can swim infinite distances in zero time.
# Of course, you must stay within the boundaries of the grid during your swim.
# Return the minimum time until you can reach the bottom right square (n - 1, n - 1)
# if you start at the top left square (0, 0).
from typing import List
from functools import cache
# Time Complexity:
# Space Complexity:

def swimInWater(self, grid: List[List[int]]) -> int:
    size = len(grid)  # how big the grid is (size x size)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    best_time = float('inf')  # track the lowest max elevation we've seen
    visited = [[False] * size for _ in range(size)]  # keep track of where we've been

    @cache
    def dfs(r, c, curr_max):
        nonlocal best_time

        # stop if out of bounds or already visited
        if r < 0 or c < 0 or r >= size or c >= size or visited[r][c]:
            return

        # update the highest elevation along this path
        curr_max = max(curr_max, grid[r][c])

        # if we're already worse than the best solution, bail out
        if curr_max >= best_time:
            return

        # if we reached the bottom-right corner, record a new best
        if r == size - 1 and c == size - 1:
            best_time = curr_max
            return

        # otherwise, keep exploring
        visited[r][c] = True
        for dr, dc in moves:
            dfs(r + dr, c + dc, curr_max)
        visited[r][c] = False

    # start from top-left, with its elevation as the initial max
    dfs(0, 0, grid[0][0])
    return best_time