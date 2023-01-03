class Solution:
    # dynammic programming
    # top-down
    def rob_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money = [0]*len(nums)
        money[0], money[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            if i-3 >= 0:
                money[i] = max(money[i-2] + nums[i], money[i-3] + nums[i])  # !!! similar to climbing stairs
            else:
                money[i] = money[i-2] + nums[i]
        return max(money[-1], money[-2])

    def rob_2(self, A):  # t.c. O(N), s.c. O(1)
        dp1, dp2 = 0, 0
        for num in A:
            dp1, dp2 = dp2, max(dp1+num, dp2)
        return dp2

    # Cleaner dp; bottom up
    def rob_3(self, A):
        dp = [0]*len(A)
        for i in range(len(A)):
            if i == 0:
                dp[i] = A[i]
            elif i == 1:
                dp[i] = max(A[i], A[i-1])  # !!!
            else:
                dp[i] = max(dp[i-1], dp[i-2]+A[i])
                # Reason why we only consider 2 entries before dp[i]:
                # If passing thru dp[i-3], we definitely need to pass thru dp[i-1] to achieve optimal value
                # (not to mention all entries before dp[i-3])
        return dp[len(A)-1]
