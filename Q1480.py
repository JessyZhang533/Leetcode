# Running sum of 1d array

import itertools


class Solution:
    def runningSum_1(self, nums: List[int]) -> List[int]:
        result_list = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1):  # Note it is i+1, because we nee access to nums[i]
                result_list[i] += nums[j]
        return result_list

    # Much less runtime
    def runningSum_2(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)
