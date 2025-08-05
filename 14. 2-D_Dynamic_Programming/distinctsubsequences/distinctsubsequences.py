# leetcode 115
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Time Complexity:
# Space Complexity:

def numDistinct(self, s: str, t: str) -> int:
    """
    Count how many distinct ways we can form string t by deleting characters from string s.
    """

    # lengths of the input strings
    len_s = len(s)
    len_t = len(t)

    # table[i][j] will hold the number of ways to form t[:j] from s[:i]
    table = [[0.0] * (len_t + 1) for _ in range(len_s + 1)]

    # Base case:
    # If t is empty (j = 0), there is exactly one way to form it from any prefix of s:
    # delete all characters in that prefix.
    for i in range(len_s + 1):
        table[i][0] = 1.0

    # Fill the rest of the table
    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                # When the current characters match,
                # we can either use this character (table[i-1][j-1])
                # or skip it (table[i-1][j]).
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
            else:
                # If they don't match, we must skip s[i-1],
                # so inherit the count from table[i-1][j].
                table[i][j] = table[i - 1][j]

    # The final answer is the number of ways to form all of t from all of s
    return int(table[len_s][len_t])