class Solution:
    # Dynamic Programming
    # Use the solution of Q198 House Robber as a helper function
    def rob_1(self, nums: List[int]) -> int:
        def rob_helper(A):
            if not A:
                return 0
            dp = [0]*(len(A))
            for i in range(len(A)):
                if i == 0:
                    dp[i] = A[i]
                elif i == 1:
                    dp[i] = max(A[i], A[i-1])  # !!!
                else:
                    dp[i] = max(dp[i-1], dp[i-2]+A[i])
            return dp[len(A)-1]
        return max(rob_helper(nums[2:-1])+nums[0], rob_helper(nums[1:]))

    # Same thing as method 1 but without a list
    def rob_2(self, nums):
        def rob_helper(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)
            return dp2
        return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))
        