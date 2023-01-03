from collections import Counter


class Solution_1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = Counter(nums), 0, 0  # points is a dict
        for value in range(max(points.keys()) + 1):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr

class Solution_2(object):
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr

    def deleteAndEarn(self, nums):
        points = [0] * 10001  # largest entry possible is 10000 stated in the question constraint
        for num in nums:
            points[num] += num
        return self.rob(points)
