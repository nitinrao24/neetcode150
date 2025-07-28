# leetcode 79
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Time Complexity:
# Space Complexity:
def wordSearch(board,word):
    grid = board
    rows = len(grid)
    cols = len(grid[0])
    target = word
    length = len(target)

    def dfs(r, c, idx):
        if idx == length:
            return True

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != target[idx]:
            return False

        saved = grid[r][c]
        grid[r][c] = ''

        found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
        )

        grid[r][c] = saved
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False

print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))