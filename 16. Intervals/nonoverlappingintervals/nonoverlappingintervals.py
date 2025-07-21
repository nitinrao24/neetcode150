# leetcode 435
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Time Complexity:
# Space Complexity:

def nonOverlappingIntervals(intervals):
    res = 0
    decorated = []
    for interval in intervals:
        decorated.append((interval[1], interval))
    decorated.sort()
    sorted_intervals = []
    for pair in decorated:
        sorted_intervals.append(pair[1])
    prev_end = sorted_intervals[0][1]
    for interval in sorted_intervals[1:]:
        if prev_end > interval[0]:
            res += 1
        else:
            prev_end = interval[1]
    return res

print(nonOverlappingIntervals([[1,2],[2,3],[3,4],[1,3]]))