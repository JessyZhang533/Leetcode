from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, mul))
        suf = list(accumulate(nums[::-1], mul))[::-1]  # .reverse() & [::-1]: the former reverse the list inplace, the latter creates a new list which is the reversed original
        n = len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i<n-1 else 1) for i in range(n)]
