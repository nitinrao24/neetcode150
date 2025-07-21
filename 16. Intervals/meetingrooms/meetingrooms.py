# leetcode 252
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# determine if a person could add all meetings to their schedule without any conflicts.

# Time Complexity:
# Space Complexity:

def meetingRooms(intervals):
    intervals.sort()

    for idx in range(1, len(intervals)):
        prev_interval = intervals[idx - 1]
        curr_interval = intervals[idx]
        prev_end = prev_interval[1]
        curr_start = curr_interval[0]
        if prev_end > curr_start:
            return False

    return True

print(meetingRooms([(0,30),(5,10),(15,20)]))