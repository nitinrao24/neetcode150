# leetcode 253
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# find the minimum number of days required to schedule all meetings without any conflicts.

def meetingRooms2(intervals):
    n = len(intervals)

    start_times = []
    end_times = []
    for interval in intervals:
        start_times.append(interval[0])
        end_times.append(interval[1])

    start_times.sort()
    end_times.sort()

    max_rooms = 0
    current_rooms = 0

    s_ptr = 0
    e_ptr = 0

    while s_ptr < n:
        if start_times[s_ptr] < end_times[e_ptr]:
            current_rooms += 1
            s_ptr += 1
        else:
            current_rooms -= 1
            e_ptr += 1
        if current_rooms > max_rooms:
            max_rooms = current_rooms

    return max_rooms

print(meetingRooms2([(0,40),(5,10),(15,20)]))