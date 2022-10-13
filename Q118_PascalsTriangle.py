class Solution_1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = self.generate(numRows-1)
        nth_row = [1]*numRows
        for i in range(1, numRows-1):
            nth_row[i] = res[-1][i-1] + res[-1][i]
        res.append(nth_row)
        return res

from operator import add  # !!!
class Solution_2:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for _ in range(1, numRows):
            map_ = map(add, [0] + res[-1], res[-1] + [0])  # !!!: eg.[0, 1, 3, 3, 1] + [1, 3, 3, 1, 0] = [1, 4, 6, 4, 1]
            res.append(list(map_))  # convert to list. map_ is just an object stored at an address
        return res if numRows else []