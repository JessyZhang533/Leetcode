class Solution:
    # dp
    def getMaxLen_1(self, nums: List[int]) -> int:
        " s.c. O(1) "
        n = len(nums)
        pos, neg = 0, 0
        if nums[0] > 0: pos = 1
        if nums[0] < 0: neg = 1
        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos  # !!! cannot write in split paragraphs like the format as above
                # because when we write neg = 1 + pos explicitly, pos is already the new value, but we want the old value here
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans

    def getMaxLen_2(self, nums: List[int]) -> int:
        " s.c. O(n) "
        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]  # if pos[i-1]==0, we only need to add 1 as in other cases
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0  # if neg[i-1]==0, we need neg[i]==0
            elif nums[i] < 0:  # don't have the problem here as method 1
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans
