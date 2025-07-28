# leetcode 134
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost,
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# Time Complexity: O(n)
# Space Complexity: O(n)

def gasStation(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    fuel = 0
    start_station = 0

    for station in range(len(gas)):
        fuel += gas[station] - cost[station]
        if fuel < 0:
            fuel = 0
            start_station = station + 1

    return start_station

print(gasStation([1,2,3,4,5],[3,4,5,1,2]))