class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0

        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
			# either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
        # maximum profit must be in not-hold state
        return cur_not_hold

    def maxProfit_2(self, prices: List[int]) -> int:
        price_gain = []
        for idx in range(len(prices)-1):
            if prices[idx] < prices[idx+1]:
                price_gain.append(prices[idx+1]- prices[idx])
        return sum(price_gain)
