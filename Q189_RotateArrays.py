class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        " Use pointers to swap. Correct but time limit exceeded "
        def rotate_by_one(nums):
            prev = nums[-1]
            for i in range(len(nums)):
                curr = nums[i]
                nums[i] = prev
                prev = curr
            return nums
        for _ in range(k):
            rotate_by_one(nums)
        return nums