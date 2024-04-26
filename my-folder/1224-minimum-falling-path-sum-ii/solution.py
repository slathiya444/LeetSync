class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal dp, m, n

            # base1; last row so return the cell value
            if i == m - 1:
                return grid[i][j]

            # seen before
            if dp[i][j] != -1:
                return dp[i][j]

            # otherwise compute dp[i][j]
            res = float('inf')
            for col in range(n):
                # pass; same column as j
                if col == j:
                    continue

                # get the current cell value and go to next row i + 1
                temp = grid[i][j] + dfs(i + 1, col)

                # compare
                res = min(res, temp)

            # update
            dp[i][j] = res

            return dp[i][j]

        m, n = len(grid), len(grid[0])

        # dp[i][j] := minimum sum of a falling path with non-zero shifts starting at cell (i, j)
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        minSum = float('inf')

        # run dfs for each possible col on first row
        for j in range(n):
            temp = dfs(0, j)
            minSum = min(minSum, temp)

        return minSum
