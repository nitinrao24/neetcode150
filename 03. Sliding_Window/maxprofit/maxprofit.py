# leetcode 121
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Time Complexity:
# Space Complexity

def maxProfit(prices):
    if not prices:
        return 0

    maxProf = 0
    minbuy = prices[0]
    for i in range(1, len(prices)):
        maxProf = max(maxProf, prices[i] - minbuy)
        minbuy = min(minbuy, prices[i])
    return maxProf

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

