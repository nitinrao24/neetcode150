# leetcode 70
# You are climbing a staircase with n steps. At each step, you can either climb 1 or 2 steps.
# Your task is to determine the number of distinct ways you can climb to the top.

def climbingStairs(n):
    if n <= 3:
        return n
    one_before = 3
    two_before = 2
    current = 0
    for i in range(3, n):
        current = one_before + two_before
        two_before = one_before
        one_before = current
    return current

print(climbingStairs(2))
print(climbingStairs(3))
print(climbingStairs(4))