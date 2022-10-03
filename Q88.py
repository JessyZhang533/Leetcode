# Merge sorted arrays

# From max value to min value
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:  # Don't need case where m>0, cause then we don't need to modify nums1
            nums1[:n] = nums2[:n]

# NO need to worry about overwriting in nums1:
# Say we've filled the last n items in nums1, which means taht we've aleady sorted out the n largest values of the two lists.
# Say these n values have i values from nums1 and (n-i) values from nums2.
# Then now we have i extra spaces in nums 1, and we still have i values in nums2 needing to be moved to nums1, i==i, perfect.
