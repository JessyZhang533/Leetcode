from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        res = 0
        rotten = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        while rotten and fresh>0:
            res += 1  # one minite passes every time enter the while loop
            for _ in range(len(rotten)):  # iterate through all the 'old' rotten oranges in this current minute
                x, y = rotten.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # !!! learn this technique
                    xx, yy = x+dx, y+dy
                    if xx < 0 or yy < 0 or xx > m-1 or yy > n-1:
                        continue
                    elif grid[xx][yy] == 2 or grid[xx][yy] == 0:
                        continue
                    else:
                        fresh -= 1
                        grid[xx][yy] = 2
                        rotten.append((xx, yy))  # append 'new' rotten orange
        return res if fresh == 0 else -1
