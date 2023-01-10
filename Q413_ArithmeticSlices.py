class Solution:
    def numberOfArithmeticSlices_1(self, nums: List[int]) -> int:
        " dp; here dp[i] represents the number of required subarrays in nums[:i] "
        dp = [0]*len(nums)
        for i in range(2, len(nums)):
            if (nums[i]-nums[i-1]) == (nums[i-1]-nums[i-2]):
                dp[i] = 2*dp[i-1]-dp[i-2]+1  # dp[i]-dp[i-1] = dp[i-1]-dp[i-2]+1
            else:
                dp[i] = dp[i-1]
        return dp[-1]  # compare with method 2

    def numberOfArithmeticSlices_2(self, nums: List[int]) -> int:
        " dp; here dp[i] represents the number of required subarrays ending with nums[i] "
        dp = [0]*len(nums)
        for i in range(2, len(nums)):
            if (nums[i]-nums[i-1]) == (nums[i-1]-nums[i-2]):
                dp[i] = dp[i-1]+1  # !!!
        return sum(dp)  # compare with method 1
