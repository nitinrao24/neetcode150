# leetcode 322
#You are given an integer array coins
# representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# Time Complexity:
# Space Complexity:

def coinChange(coins,amount):
    max_amount = amount + 1
    min_coins_needed = [max_amount] * (amount + 1)
    min_coins_needed[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if current_amount - coin >= 0:
                candidate = min_coins_needed[current_amount - coin] + 1
                if candidate < min_coins_needed[current_amount]:
                    min_coins_needed[current_amount] = candidate

    result = min_coins_needed[amount]
    if result == max_amount:
        return -1
    return result

print(coinChange([1,2,5],11))