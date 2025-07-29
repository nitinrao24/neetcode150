# leetcode 567
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Time Complexity: O(n)
# Space Complexity: O(1)

def permutationinString(self, s1: str, s2: str) -> bool:
    # If the pattern is longer than the text, it can't fit
    if len(s1) > len(s2):
        return False

    # Prepare two 26‑slot lists to count letters a–z
    count1 = [0] * 26  # letter counts for s1
    count2 = [0] * 26  # letter counts for the current window in s2

    # Initialize counts using the first window of length len(s1)
    for i in range(len(s1)):
        count1[ord(s1[i]) - ord('a')] += 1  # add one for s1[i]
        count2[ord(s2[i]) - ord('a')] += 1  # add one for s2[i]

    # If the counts match right away, we found a permutation
    if count1 == count2:
        return True

    # Slide the window forward one character at a time
    for i in range(len(s1), len(s2)):
        # Include the new right‑end character
        count2[ord(s2[i]) - ord('a')] += 1
        # Exclude the old left‑end character
        count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        # Check for a match again
        if count1 == count2:
            return True

    # No matching window found
    return False


def permutationinString1(s1, s2):
    w = ''
    for j in range(len(s2)):
        w += s2[j]
        if len(w) > len(s1):
            w = w[1:]
        if len(w) == len(s1) and sorted(w) == sorted(s1):
            return True
    return False

print(permutationinString("ab", "eidbaooo"))
print(permutationinString("ab", "eidboaoo"))