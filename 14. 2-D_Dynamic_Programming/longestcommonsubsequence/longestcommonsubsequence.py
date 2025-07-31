# leetcode 1143
# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters
# (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# Time Complexity:
# Space Complexity:

def longestCommonSubsequence(text1, text2):
    # lcs_array[i] stores best length ending at text1[i] so far
    lcs_array = [0] * len(text1)

    # overall longest common subsequence length
    max_len = 0

    # iterate characters in text2
    for ch in text2:
        prev_best = 0  # best value to the "left" before potential match

        # iterate over text1 by index (no enumerate)
        for i in range(len(text1)):
            char1 = text1[i]

            if prev_best < lcs_array[i]:
                prev_best = lcs_array[i]
            elif ch == char1:
                new_length = prev_best + 1
                lcs_array[i] = new_length

                if new_length > max_len:
                    max_len = new_length

    # return the length of longest common subsequence
    return max_len

print(longestCommonSubsequence("abcde","ace"))