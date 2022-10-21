class Solution:
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        """
        # https://leetcode.com/problems/first-missing-positive/solutions/17080/python-o-1-space-o-n-time-solution-with-explanation/?orderBy=most_votes
        nums.append(0)  # not necessary; see method 2
        n = len(nums)
        # 1st for loop: make all values in nums between 0 and n-1 
        for i in range(n):
            if nums[i] <= 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n  # !!!
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n

    def firstMissingPositive_2(self, nums: List[int]) -> int:
        """
        For nums with length n, the possible result is in the range of
        [1 : n + 1], we want to know the smallest integer in the range 
        of [1 : n] that is not in nums, if [1 : n] are all in nums,
        the result is n + 1
        
        So those numbers not in [1 : n] are not useful and we can just
        change them to be 0
        
        Then we go through nums, if nums[i] is in the range of 
        [1 : n], we use index (nums[i] - 1) to record that we have
        seen nums[i] by adding n + 1 to nums[nums[i] - 1]
        
        Finally we just need to find the first index i for which 
        nums[i] is less than n + 1 (which means we never met number
        i + 1 so we did not add n + 1 to nums[i])
        """
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            if 1 <= nums[i] % (n + 1) <= n:
                ind = nums[i] % (n + 1) - 1
                nums[ind] += n + 1
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        return n + 1
