# leetcode 62
# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n,
# return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# Time Complexity:
# Space Complexity:

def uniquePaths(m,n):
    # initialize the first row: there is exactly 1 way to reach each cell in row 0
    previous = [1] * n

    # build rows one by one
    for _ in range(m - 1):
        current = [1] * n  # first column is always 1
        for col in range(1, n):
            # number of ways to reach this cell is from left + from top
            current[col] = current[col - 1] + previous[col]
        previous = current  # move down

    # answer is number of ways to reach bottom-right corner
    return previous[-1]

print(uniquePaths(3,7))