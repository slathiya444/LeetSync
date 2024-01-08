class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(row, col):
            ## base cases
            if row == m-1 and col == n-1:
                return 1
            elif row == m or col == n or obstacleGrid[row][col]:
                return 0
            ## recurance relatoions
            return dp(row+1, col) + dp(row, col+1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        return dp(0, 0)
        
