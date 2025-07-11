# leetcode 49
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict
from typing import List
# Time Complexity
# Space Complexity

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)

    return ans.values()