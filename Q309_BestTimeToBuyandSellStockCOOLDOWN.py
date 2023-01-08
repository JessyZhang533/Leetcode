class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        # own[i] represents the maximum profit for the first i days if we own a stock at the end of day[i].
        # not_own[i] represents the maximum profit for the first i days if we do not own a stock at the end of day[i]
        own = [0]*len(prices)
        own[0] = -prices[0]  # initialise 1st entry: if we buy the stock on day 0, then our profit = -prices[0]
        not_own = [0]*len(prices)  # no need to initialise 1st entry: if we donnot buy the stock on day 0, then our profit = 0
        for i in range(1, len(prices)):
            own[i], not_own[i] = max(own[i-1], not_own[i-2] - prices[i]), max(not_own[i-1], own[i-1] + prices[i])
        return max(own + not_own)

# On day[i], we can choose cooldown, buy, or sell:
# 1. Under what condition we can choose to cooldown on day[i]?
# It is obvious, there is not requirement. We can choose to cooldown on anyday.
# 2. Under what condition we can choose to buy a stock on day[i]?
# The answer is we need make sure that we do not own any stock at end of day[i-2] because there is one day cooldown requirement.
# 3. Under what condition we can choose to sell a stock on day[i]?
# The answer is we must own a stock at the end of day[i-1].