from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # https://leetcode.com/problems/sliding-window-maximum/solutions/65901/9-lines-ruby-11-lines-python-o-n/
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res