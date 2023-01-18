import bisect


class Solution:
    def lengthOfLIS_1(self, nums: List[int]) -> int:  # t.c. O(N^2)
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    # bisect_left():  finds and returns the position at which an element can be inserted into a Python list while maintaining the sorted order of the Python list
    def lengthOfLIS_2(self, nums: List[int]) -> int:  # t.c. O(NlogN)
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:  # if len(sub)>=0 and sub[-1] >= x, then a new subsequence will begin to rewrite the old 'sub'. However, as long as the new sequence is not as long, the length of the old 'sub' will be preserved
                idx = bisect.bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)
