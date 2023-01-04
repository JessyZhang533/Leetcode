class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # top-down approach: start from the end of list, see if can reach the beginning of list
        last_pos = len(nums) - 1  # last_pos is the essentially the smallest index that can reach the end of list
        for i in range(len(nums)-2, -1, -1):
            if (i + nums[i]) >= last_pos:
                last_pos = i
        return last_pos == 0

    # time limit exceeded, but intruduces a top-down dp solution
    # dp[i] represents whether we can reach the end of list
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for i in range(n-2, -1, -1):
            for j in range(i+1, min(n, i+nums[i]+1)):  # check indices (i+1) --> (n-1) or (i+nums[i])
                if dp[j]:  # if any entries in the above range is True, then it means we can reach the end of list from d[i]
                    dp[i] = True
                    break
        return dp[0]
