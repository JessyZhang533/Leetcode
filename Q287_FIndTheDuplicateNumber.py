class Solution:
    def findDuplicate_1(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                return i
            else:
                dic[i] = True

    def findDuplicate_2(self, nums):  # t.c. O(nlogn); s.c. O(1)
        # Originally, there are n+1 objects and n holes, this condition complies to pigeonhole principle, so at least one hole has two objects, that is one number appears twice.
        # In each iteration, the algorithm finds the number of objects that should be filled into the first n/2 holes.
        # If this number k >= n/2+1, then this is complies to pigeonhole principle again, we search this subproblem.
        # otherwise, consider the remaining n/2 holes and remaining objects to fill. Because k <= n/2, the number of remaining objects is r=(n+1)-k>=n/2+1, that is, the remaining objects and remaining n/2 holes complies to pigeonhole principle again, we just need to search this subproblem.
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums)-1

        while low < high:
            mid = (high + low) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
