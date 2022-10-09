class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = True
        return False

    def containsDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))  # !!! set does not allow duplicates