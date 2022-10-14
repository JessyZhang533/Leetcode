class Solution:
    def runningSum_1(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

    def runningSum_2(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return accumulate(nums)

    def runningSum_3(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]  # run time a lot better than the first method!
        return nums
    