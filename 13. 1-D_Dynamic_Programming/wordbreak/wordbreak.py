# leetcode 139
# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Time Complexity:
# Space Complexity:

def wordBreak(s,wordDict):
    can_break = [True] + [False] * len(s)

    for end in range(1, len(s) + 1):
        for word in wordDict:
            start = end - len(word)
            if start >= 0 and can_break[start] and s[start:end] == word:
                can_break[end] = True
                break

    return can_break[-1]

print(wordBreak("leetcode", ["leet", "code"]))