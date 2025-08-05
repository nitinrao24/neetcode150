# leetcode 10
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Time Complexity:
# Space Complexity:

def isMatch(self, s: str, p: str) -> bool:
    """
    Return True if the string s matches the pattern p.
    In p, '.' matches any single character and '*' matches zero or more of the preceding element.
    """

    # lengths of the string and the pattern
    str_len = len(s)
    pat_len = len(p)

    # dp[i][j] will be True if s[:i] matches p[:j]
    dp = [[False] * (pat_len + 1) for _ in range(str_len + 1)]

    # empty string matches empty pattern
    dp[0][0] = True

    # handle patterns like a*, a*b*, etc. matching the empty string
    for pat_idx in range(2, pat_len + 1):
        is_star = (p[pat_idx - 1] == '*')
        if is_star:
            # we can ignore the preceding char and the '*'
            dp[0][pat_idx] = dp[0][pat_idx - 2]

    # fill dp table for each prefix of s and p
    for str_idx in range(1, str_len + 1):
        for pat_idx in range(1, pat_len + 1):

            current_pat_char = p[pat_idx - 1]
            if current_pat_char == '*':
                # case 1: '*' counts as zero occurrence of p[pat_idx-2]
                use_zero = dp[str_idx][pat_idx - 2]

                # case 2: '*' counts as one or more, so s[str_idx-1] must match p[pat_idx-2]
                prev_pat_char = p[pat_idx - 2]
                matches_prev = (prev_pat_char == '.' or prev_pat_char == s[str_idx - 1])
                if matches_prev:
                    use_one_or_more = dp[str_idx - 1][pat_idx]
                else:
                    use_one_or_more = False

                dp[str_idx][pat_idx] = use_zero or use_one_or_more

            else:
                # for non-'*' patterns, match single character or '.'
                matches_char = (current_pat_char == '.' or current_pat_char == s[str_idx - 1])
                if matches_char:
                    dp[str_idx][pat_idx] = dp[str_idx - 1][pat_idx - 1]
                else:
                    dp[str_idx][pat_idx] = False

    # final answer: whether full s matches full p
    return dp[str_len][pat_len]