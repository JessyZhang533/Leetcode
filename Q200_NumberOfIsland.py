# Number of islands

class Solution(object):
    # Use depth first search
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        def dfs(i, j):
            " If the input pixel grid[i][j] is '1', i.e. land, then dfs would change the whole island where the pixel is in from False to True (in 'visited') "
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:  # 6 conditions
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == '1':  # The grid is surrounded by water, so once 1 appears it must be in an island
                    dfs(i, j)
                    count += 1
        return count
