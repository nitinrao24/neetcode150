# leetcode 57
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Time Complexity:
# Space Complexity:

def insertIntervals(intervals, newInterval):
    result = []
    for interval in intervals:
        if interval[1] < newInterval[0]:
            result.append(interval)
        elif interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    result.append(newInterval);
    return result

print(insertIntervals([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))