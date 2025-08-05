# leetcode 981
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Time Complexity: O(1) for set, O(log m) for get
# Space Complexity: O(n)

from bisect import bisect_right
from typing import List

class TimeMap:
    def __init__(self):
        # Create an empty dict to hold each key’s timestamps and values
        # Format: key → {'times': [...], 'values': [...]}
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If this key hasn’t been seen yet, initialize its lists
        if key not in self.store:
            self.store[key] = {'times': [], 'values': []}
        # Append the timestamp to the key’s time list
        self.store[key]['times'].append(timestamp)
        # Append the corresponding value to the key’s value list
        self.store[key]['values'].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn’t exist at all, return an empty string
        if key not in self.store:
            return ""
        # Grab the sorted list of times and parallel list of values
        times = self.store[key]['times']
        values = self.store[key]['values']
        # Find how many stored times are ≤ the given timestamp
        # bisect_right returns the insertion index to keep times sorted
        idx = bisect_right(times, timestamp)
        # If idx is 0, no stored timestamp is ≤ the given one → return ""
        if idx == 0:
            return ""
        # Otherwise, the answer is the value at index idx-1
        return values[idx - 1]


class TimeMap1:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        entries = self.store.get(key, [])
        left = 0
        right = len(entries) - 1

        while left <= right:
            mid = (left + right) // 2
            entry_time = entries[mid][1]
            if entry_time <= timestamp:
                result = entries[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)