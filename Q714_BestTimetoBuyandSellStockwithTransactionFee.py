class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        not_own = 0
        own = -prices[0]
        for i in prices:
            own, not_own = max(own, not_own-i), max(not_own, own+i-fee)
            res = max(res, own, not_own)
        return res
