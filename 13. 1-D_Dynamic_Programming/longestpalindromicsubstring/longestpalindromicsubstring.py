# leetcode 5
# Given a string s, return the longest palindromic substring in s.

# Time Complexity:
# Space Complexity:

def longestPalindromicSubstring(string):
    if not string:
        return ""

    def expand(string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    end = 0
    length = len(string)

    for center in range(length):
        odd_len = expand(string, center, center)
        even_len = expand(string, center, center + 1)

        max_len = odd_len if odd_len > even_len else even_len

        current_span = end - start
        if max_len > current_span:
            start = center - (max_len - 1) // 2
            end = center + max_len // 2

    return string[start:end + 1]

print(longestPalindromicSubstring("babaa"))