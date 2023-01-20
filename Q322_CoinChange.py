class Solution:
    # Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
    def coinChange_1(self, coins, amount):
        MAX = float('inf')  # infinity
        dp = [0] + [MAX] * amount  # !!!: create a list

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]  # dp[amount]==MAX, then the index = 1; otherwise =0. Equivalent to an if statement

    def coinChange_2(self, coins, amount):
        " explanation of method 1 "
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1):
            prev = MAX
            for c in coins:
                if i >= c:
                    prev = min(prev, dp[i-c])
            dp[i] = prev + 1
        print(dp)
        return [dp[amount], -1][dp[amount]==MAX]
