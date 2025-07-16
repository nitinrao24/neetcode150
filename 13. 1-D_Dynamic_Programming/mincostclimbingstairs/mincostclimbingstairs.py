# leetcode 746
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.

def minCostClimbingStairs(cost):
    cost.append(0)
    for i in range(len(cost) - 4, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))