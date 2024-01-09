class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache
        def dp(row, col):
            ## base cases
            if row < 0 or col < 0:
                return float('inf')

            elif row == 0 and col == 0:
                return grid[row][col]

            ## recurance relation
            return grid[row][col] + min(dp(row-1, col), dp(row, col-1))

        m, n = len(grid), len(grid[0])
        return dp(m-1, n-1)
        
