class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1  # handle base case i==c

        # The sequence of outer and inner for loop cannot be flipped! Otherwise combinations will be counted repeatedly
        # for example, if we iterate i in the outer for loop and c in the inner for loop:
        # to create 7:
        # When amount is 2 and the coin value is 5, it would be counted as 1 way.
        # When amount is 5 and the coin value is 2, the number of ways become 2.
        for c in coins:
            for i in range(1, amount+1):
                if i >= c:
                    dp[i] += dp[i-c]
        return dp[-1]
