# leetcode 567
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Time Complexity:
# Space Complexity:

def permutationinString(s1, s2):
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