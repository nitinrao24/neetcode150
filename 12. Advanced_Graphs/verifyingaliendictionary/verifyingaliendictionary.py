# leetcode 953
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.

# Time Complexity:
# Space Complexity:
from typing import List
def isAlienSorted(self, words: List[str], order: str) -> bool:
    # first, build a lookup so we know each letter’s rank in the alien alphabet
    rank = {}
    for i in range(len(order)):
        rank[order[i]] = i

    # now check every neighboring pair of words
    for w in range(len(words) - 1):
        first = words[w]
        second = words[w + 1]

        # compare letters one by one
        for idx in range(len(first)):
            # if second word is shorter but has all the same letters so far, it’s out of order
            if idx == len(second):
                return False

            # once letters differ, we can decide their order
            if first[idx] != second[idx]:
                if rank[first[idx]] > rank[second[idx]]:
                    return False
                # this pair is in correct order, move on to the next pair
                break

    # if we never found a problem, the list is sorted
    return True