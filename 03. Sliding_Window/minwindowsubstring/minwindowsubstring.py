# leetcode 76
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# Time Complexity:
# Space Complexity:

from collections import defaultdict

def minWindowSubstring(s, t):
    if len(s) < len(t):
        return ""

    count = defaultdict(int)

    for char in t:
        count[char] += 1

    needed = len(t)
    best_start = 0
    best_end = float("inf")
    start = 0

    for end in range(len(s)):
        char = s[end]
        if count[char] > 0:
            needed -= 1
        count[char] -= 1

        if needed == 0:
            while True:
                start_char = s[start]
                if count[start_char] == 0:
                    break
                count[start_char] += 1
                start += 1

            if end - start < best_end - best_start:
                best_start = start
                best_end = end

            count[s[start]] += 1
            needed += 1
            start += 1

    if best_end > len(s):
        return ""
    return s[best_start:best_end + 1]

print(minWindowSubstring("ADOBECODEBANC", "ABC"))