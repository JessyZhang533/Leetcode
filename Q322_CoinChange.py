class Solution:
    # Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
    def coinChange(self, coins, amount):
        MAX = float('inf')  # infinity
        dp = [0] + [MAX] * amount  # !!!: create a list

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
