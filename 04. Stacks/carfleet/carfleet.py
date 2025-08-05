# leetcode 853
# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n,
# where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other.
# The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.
from typing import List
# Time Complexity: O(n log n)
# Space Complexity: O(n)

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # Pair up each car's position with its speed and sort by position descending
    # so we process cars closest to the target first.
    cars = sorted(zip(position, speed), reverse=True)  # list of (pos, speed) from largest pos to smallest

    fleets = 0                  # count of distinct fleets formed
    last_arrival = -1.0         # arrival time of the fleet ahead; start with sentinel that any real time is larger

    # Go through each car in order from nearest to target backward
    for pos, spd in cars:
        # Compute how long this car would take to reach the target if unobstructed
        arrival_time = (target - pos) / spd

        # If this car takes longer than the fleet ahead, it cannot catch up and becomes a new fleet
        if arrival_time > last_arrival:
            fleets += 1               # new fleet is formed
            last_arrival = arrival_time  # update the leading fleet's arrival time
        # Otherwise, this car joins the fleet ahead (do nothing)

    return fleets

def carFleet1(target,position,speed):
    car_list = []
    for pos, spd in zip(position, speed):
        car_list.append([pos, spd])
    arrival_times = []
    sorted_cars = sorted(car_list)[::-1]
    for pos, spd in sorted_cars:
        arrival_time = (target - pos) / spd
        if not arrival_times or arrival_time > arrival_times[-1]:
            arrival_times.append(arrival_time)

    return len(arrival_times)

print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))