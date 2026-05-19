def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(
                dp[value],
                dp[value - coin] + 1
            )

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Minimum Coins Needed:",
      coin_change(coins, amount))
