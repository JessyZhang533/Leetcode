class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/178422/one-pass/
        # 2 scenarios:
        # 1. subarray in the middle of nums; same as Q53 Maximum Subarray
        # 2. subarray is cut by the end of nums (circular); this time we need to find the min array in the middle of nums using the same method as Q53
        # Proof of scenario 2:
        # max(prefix+suffix) = max(total sum - subarray) = total sum + max(-subarray) = total sum - min(subarray)
        # NOTE: 
        # If all numbers are negative, maxSum = max(A) and minSum = sum(A).
        # In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
        # According to the deacription, We need to return the max(A), instead of sum of am empty subarray.
        # So we return the maxSum to handle this corner case.
        dp1, dp2 = [*nums], [*nums]  # dp1 for the max subarray (middle), dp2 for the min array (middle)
        for i in range(1, len(nums)):
            dp1[i] = max(nums[i], nums[i]+ dp1[i-1])
            dp2[i] = min(nums[i], nums[i]+ dp2[i-1])
        max_number = max(nums)
        total = sum(nums)
        return max(max(dp1), total-min(dp2)) if max_number > 0 else max_number
