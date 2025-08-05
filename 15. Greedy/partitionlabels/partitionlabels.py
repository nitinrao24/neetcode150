# leetcode 763
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# For example, the string "ababcc" can be partitioned into ["abab", "cc"],
# but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
# Note that the partition is done so that after concatenating all the parts in order,
# the resultant string should be s.
# Return a list of integers representing the size of these parts.

# Time Complexity:
# Space Complexity:

def partitionLabels(s):
    last_pos = {}
    for i in range(len(s)):
        last_pos[s[i]] = i

    idx = 0
    lengths = []

    while idx < len(s):
        end = last_pos[s[idx]]
        length = 0

        while idx <= end:
            if last_pos[s[idx]] > end:
                end = last_pos[s[idx]]
            idx += 1
            length += 1

        lengths.append(length)

    return lengths
