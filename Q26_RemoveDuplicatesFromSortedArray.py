class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        s, f = 1, 1  # s points at the position right after the 'no-duplicate' array
        n = len(nums)
        if n == 1:  # handle edge case
            return 1
        curr_num = nums[0]
        while f < n:
            if nums[f] == curr_num:
                f += 1
            else:
                curr_num = nums[f]
                nums[s], nums[f] = nums[f], nums[s]
                f += 1
                s += 1
        return s

    def removeDuplicates_2(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]  # we don't care about what we leave beyong the returned k, so no need to modify nums[i+1] 
                x += 1
        return x
