# leetcode 1046
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Time Complexity:
# Space Complexity:

def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()  # ascending
        y = stones.pop()  # largest
        x = stones.pop()  # 2nd largest
        if x != y:
            stones.append(y - x)
    if len(stones) > 0:
        return stones[0]
    else:
        return 0

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))