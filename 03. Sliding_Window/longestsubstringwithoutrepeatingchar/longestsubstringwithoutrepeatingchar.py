# leetcode 3
# Given a string s, find the length of the longest substring without duplicate characters.

# Time Complexity: O(n)
# Space Complexity: O(n)

def longestSubstringWithoutRepeatingChar(str):
    i = 0
    best = 0
    seen = set()

    for j in range(len(str)):
        while str[j] in seen:
            seen.remove(str[i])
            i += 1

        seen.add(str[j])
        best = max(best, j - i + 1)

    return best

print(longestSubstringWithoutRepeatingChar("pwwkew"))
print(longestSubstringWithoutRepeatingChar("abcabcbb"))
print(longestSubstringWithoutRepeatingChar("bbbbb"))