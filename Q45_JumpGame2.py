class Solution:
    def jump_1(self, nums: List[int]) -> int:
        # dp; dp[i] is the minimum number of steps required to jump from index i to the end
        # if dp[i] == inf, it means cannot reach the end from index i
        n = len(nums)
        dp = [0]*n
        for i in range(len(nums)-2, -1, -1):
            if i+1 < min(n, i+nums[i]+1):
                dp[i] = 1 + min(dp[(i+1) : min(n, i+nums[i]+1)])
            else:  # means cannot reach the end
                dp[i] = float('inf')
        return dp[0]

    def jump_2(self, nums: List[int]) -> int:
        # two pointers l & r.
        # range between l & r are the points reachable in the nth jump
        # the initial range (after 0th jump) is [0,0]
        l = r = 0
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(l,r+1)])
            l,r = r+1, furthest
        return nJumps
        # Time complexity: O(N)
        # Space complexity: O(1)
