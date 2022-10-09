class Solution:
    # Quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        if not nums:
            return
        pivot = random.choice(nums)  # !!!
        # Partition into 3 groups
        left =  [x for x in nums if x > pivot]  # O(n)
        mid  =  [x for x in nums if x == pivot]  # O(n)
        right = [x for x in nums if x < pivot]  # O(n)
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)  # recursion
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)# recursion
        else:
            return mid[0]