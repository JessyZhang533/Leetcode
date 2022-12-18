from collections import Counter


class Solution:
    # Counter: A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    def intersect_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        " Hashmap "
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        cnt = Counter(nums2)
        ans = []
        for x in nums1:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1  # !!!
        return ans

    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        " Two pointers "
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans