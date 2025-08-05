# leetcode 97
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively,
# such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

# Time Complexity:
# Space Complexity:

def interLeavingString(s1,s2,s3):
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)

    if n1 + n2 != n3:
        return False

    table = [[False] * (n2 + 1) for _ in range(n1 + 1)]
    table[0][0] = True

    for j in range(1, n2 + 1):
        prev = table[0][j - 1]
        match = s2[j - 1] == s3[j - 1]
        table[0][j] = prev and match

    for i in range(1, n1 + 1):
        prev = table[i - 1][0]
        match = s1[i - 1] == s3[i - 1]
        table[i][0] = prev and match

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            use_first = table[i - 1][j]
            cond1 = s1[i - 1] == s3[i + j - 1]
            use_second = table[i][j - 1]
            cond2 = s2[j - 1] == s3[i + j - 1]
            table[i][j] = (use_first and cond1) or (use_second and cond2)

    return table[n1][n2]