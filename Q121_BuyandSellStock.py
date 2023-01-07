class Solution:
    def maxProfit_1(self,prices):
        # two pointers
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

    def maxProfit_2(self,prices):
        " Q1014 method 2 & 3; the only difference is that we can directly operate with original values here "
        dp = [0]*len(prices)
        dp[0] = prices[0]
        res = 0
        for i in range(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i-1])
            res = max(res, prices[i]-dp[i])
        return res
