# leetcode 621
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
# Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order,
# but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
# Return the minimum number of CPU intervals required to complete all tasks.

# Time Complexity:
# Space Complexity:
from collections import Counter
from typing import List
def taskScheduler(tasks,n):
    counts = Counter(tasks)
    frequencies = list(counts.values())
    max_freq = max(frequencies)
    max_count = frequencies.count(max_freq)

    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(intervals, len(tasks))

print(taskScheduler(["A","A","A","B","B","B"],2))