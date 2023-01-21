class Solution:
    # see also: Q518
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        # here we consider permutations nstead of combinations, so compared to Q518, we need to inverse the inner and outer for loops
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]
