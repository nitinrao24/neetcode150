# leetcode 49
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict
from typing import List
# Time Complexity: O(n*k)
# Space Complexity: O(n*k)

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Make an empty map from each “letter‑count signature” to its anagram list
    groups = defaultdict(list)

    # For every word in the input
    for word in strs:
        # Create a fresh count of all 26 lowercase letters, start at zero
        counts = [0] * 26

        # Tally each character in this word
        for ch in word:
            # Find the slot 0–25 for this letter and increment it
            counts[ord(ch) - ord('a')] += 1

        # Convert the 26‑element list into a bytes object (quick to hash & compare)
        signature = bytes(counts)

        # Group the word under its signature
        groups[signature].append(word)

    # Return just the lists of grouped anagrams
    return list(groups.values())

def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
    # Make an empty dictionary that maps each “signature” to a list of words
    ans = defaultdict(list)

    # Go through each word in the input list
    for s in strs:
        # Create a list of 26 zeros, one slot for each lowercase letter
        count = [0] * 26

        # Go through each character in the current word
        for ch in s:
            # Figure out which slot (0–25) corresponds to this letter and add 1
            count[ord(ch) - ord('a')] += 1

        # Turn our counts into a tuple so it can be used as a dictionary key
        key = tuple(count)

        # Add the word to the list for this signature
        ans[key].append(s)

    # Return all the grouped lists of anagrams
    return list(ans.values())

def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    return ans.values()