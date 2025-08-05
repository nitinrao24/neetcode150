# leetcode 72
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Time Complexity:
# Space Complexity:

def minDistance(self, word1: str, word2: str) -> int:
    # memo will store results of subproblems to avoid recomputing them
    memo = {}

    def rec(i, j):
        """
        Compute the minimum number of edits to convert
        the first i characters of word1 into the first j characters of word2.
        """

        # If we have already solved this subproblem, return the stored answer
        if (i, j) in memo:
            return memo[(i, j)]

        # If word1 is empty (i == 0), we need j insertions to build word2
        if i == 0:
            result = j
        # If word2 is empty (j == 0), we need i deletions to reduce word1 to empty
        elif j == 0:
            result = i
        # If the last characters match, no extra cost—move both pointers back
        elif word1[i - 1] == word2[j - 1]:
            result = rec(i - 1, j - 1)
        else:
            # Otherwise, consider all three operations and pick the cheapest:
            # 1) Delete a character from word1 (move i back)
            delete_cost = rec(i - 1, j)
            # 2) Insert a character into word1 (move j back)
            insert_cost = rec(i, j - 1)
            # 3) Replace a character in word1 (move both back)
            replace_cost = rec(i - 1, j - 1)
            # Add 1 to account for the operation itself
            result = 1 + min(delete_cost, insert_cost, replace_cost)

        # Save the computed result before returning
        memo[(i, j)] = result
        return result

    # Start the recursion from the full lengths of both words
    return rec(len(word1), len(word2))