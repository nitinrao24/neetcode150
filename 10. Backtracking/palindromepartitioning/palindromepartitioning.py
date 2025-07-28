# leetcode 131
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Time Complexity:
# Space Complexity:

def palindromePartitioning(s):
    def is_palindrome(substr):
        return substr == substr[::-1]

    def backtrack(position, current_list):
        if position == len(s):
            partitions.append(current_list[:])
            return

        for next_pos in range(position + 1, len(s) + 1):
            substr = s[position:next_pos]
            if is_palindrome(substr):
                backtrack(next_pos, current_list + [substr])

    partitions = []
    backtrack(0, [])
    return partitions

print(palindromePartitioning("aab"))