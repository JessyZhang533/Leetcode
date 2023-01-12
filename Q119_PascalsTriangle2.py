class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for i in range(rowIndex):
            dp = [x + y for x, y in zip([0]+dp, dp+[0])]
        return dp
