# leetcode 518
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return 0.

# Time Complexity:
# Space Complexity:

def coinChange2(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        # build up ways to make each amount using this coin
        for amt in range(coin, amount + 1):
            ways[amt] += ways[amt - coin]

    return ways[amount]

