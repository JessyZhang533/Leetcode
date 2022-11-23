class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:  # t.c. O(n*k)
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

    def rotate_2(self, nums: List[int], k: int) -> None:  # t.c. O(n)
        " Math "
        a = [0]*len(nums)
        for i in range(len(a)):
            a[(i+k)%len(a)] = nums[i]  # !!!
        for j in range(len(a)):
            nums[j] = a[j]

    def rotate_3(self, nums: List[int], k: int) -> None:
        " 1.Reverse whole array; 2.Reverse first k elements; 3.Reverse last len(nums)-k elements "
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k %= len(nums)  # !!! Because k might be greater than len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
