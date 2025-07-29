# leetcode 424
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter
# you can get after performing the above operations.

# Time Complexity: O(n)
# Space Complexity: O(n)

def longestRepeatingCharPlacement(str, x):
    count = [0] * 26
    maxcount = 0
    i = 0
    res = 0

    for j in range(len(str)):
        idx = ord(str[j]) - ord('A')
        count[idx] += 1

        if count[idx] > maxcount:
            maxcount = count[idx]

        while (j - i + 1) - maxcount > x:
            count[ord(str[i]) - ord('A')] -= 1
            i += 1

        if j - i + 1 > res:
            res = j - i + 1

    return res

print(longestRepeatingCharPlacement("ABAB", 2))
print(longestRepeatingCharPlacement("AABABBA", 1))