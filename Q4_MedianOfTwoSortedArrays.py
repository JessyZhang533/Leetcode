# Medians of two sorted arrays

class Solution:
    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        " Same as merge sort "
        combine = []
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                combine.append(nums1[i])
                i += 1
            else:
                combine.append(nums2[j])
                j += 1
        while i < m:
            combine.append(nums1[i])
            i += 1
        while j < n:
            combine.append(nums2[j])
            j += 1
        if (m+n)%2:
            index = (m + n) // 2
            return float(combine[index])
        else:
            index = (m + n) // 2
            return float((combine[index] + combine[index-1])/2)

    # kth smallest element
    def findMedianSortedArrays_2(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        " Return the kth smallest element of a and b combined "
        if not a:
            return b[k]
        if not b:
            return a[k]
        # ia, ib being the middle indices of nums1 and nums2
        ia, ib = len(a) // 2 , len(b) // 2
        # ma, mb being the medians of nums1 and nums2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)