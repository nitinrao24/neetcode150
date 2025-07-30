# leetcode 981
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Time Complexity:
# Space Complexity:

class TimeMap:

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