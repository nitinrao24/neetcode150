# leetcode 56
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Time Complexity:
# Space Complexity:

def mergeIntervals(intervals):
    merged_intervals = []

    intervals.sort()
    current_interval = intervals[0]

    for interval in intervals[1:]:
        start = interval[0]
        end = interval[1]
        if start <= current_interval[1]:
            current_interval[1] = max(current_interval[1], end)
        else:
            merged_intervals.append(current_interval)
            current_interval = interval

    merged_intervals.append(current_interval)
    return merged_intervals

print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))