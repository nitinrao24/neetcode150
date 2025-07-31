# leetcode 309
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Time Complexity:
# Space Complexity:

def maxProfit(prices):
    n = len(prices)
    memo = {}

    def dfs_profit(hold_price, day, cooldown):
        if day >= n:
            return 0

        key = (hold_price, day, cooldown)
        if key in memo:
            return memo[key]

        best = 0

        # buy if not holding anything and cooldown is over
        if hold_price == -1 and cooldown == 0:
            best = max(best, dfs_profit(prices[day], day + 1, 0))

        # wait: move to next day, cooldown resets to 0
        best = max(best, dfs_profit(hold_price, day + 1, 0))

        # sell if holding and selling is profitable (you only need to consider selling when holding)
        if hold_price != -1 and prices[day] > hold_price:
            profit = prices[day] - hold_price
            best = max(best, profit + dfs_profit(-1, day + 1, 1))

        memo[key] = best
        return best

    return dfs_profit(-1, 0, 0)

print(maxProfit([1,2,3,0,2]))