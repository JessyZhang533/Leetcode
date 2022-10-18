class Solution:
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)  # low and high pointers
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo  # the first index where I could insert a number n into nums to keep it sorted
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
