class Solution:
    # dp

    def uniquePathsWithObstacles_1(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*c for _ in range(r)]
        # 1st step: handle first grid
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        # 2nd step: handle first row & first column (first grid exclusive)
        for m in range(1, r):
            if obstacleGrid[m][0] == 0:
                dp[m][0] = 1
            else:
                break
        for n in range(1, c):
            if obstacleGrid[0][n] == 0:
                dp[0][n] = 1
            else:
                break
        # 3rd step: handle the rest
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        " same as previous but modify in-place & use multiplication "
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        # 1st step: handle first grid
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        # 2nd step: handle first row & first column (first grid exclusive)
        for i in range(1, r):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, c):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
        # 3rd step: handle the rest
        for m in range(1, r):
            for n in range(1, c):
                obstacleGrid[m][n] = (obstacleGrid[m-1][n]+obstacleGrid[m][n-1]) * (1-obstacleGrid[m][n])
        return obstacleGrid[-1][-1]
