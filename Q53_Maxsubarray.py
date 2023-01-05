class Solution:
    def maxSubArray_1(self, nums: List[int]) -> int:
        " Kadane's algorithm; dp "
        # The thought follows a simple rule:
        # If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
        # If the sum is negative, it has no use to the next element, so we break.
        # it is a game of sum, not the elements.
        for i in range(1, len(nums)):
            if nums[i-1] > 0:  # !!!
                nums[i] += nums[i-1]  # !!! modify nums in place
        return max(nums)

    def maxSubArray_2(self, nums: List[int]) -> int:
        " dp; essentially same as above "
        dp = [*nums]  # !!! create dp same as nums
        # dp[i] is the max sum of subarray of nums[0:i+1]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])  # same as checking if dp[i-1] is positive
        return max(dp)
