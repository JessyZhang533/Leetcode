class Solution:
    def missingNumber_1(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(-1)
        for i in range(len(nums)+1):
            if i != nums[i]:
                return i

    def missingNumber_2(self, nums: List[int]) -> int:
        " math based solution "
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)  # need to use integer division although n*(n+1) will always be even, otherwise we would get a '.0' after our answer
