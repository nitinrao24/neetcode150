# leetcode 853
# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n,
# where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other.
# The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

# Time Complexity:
# Space Complexity:

def carFleet(target,position,speed):
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