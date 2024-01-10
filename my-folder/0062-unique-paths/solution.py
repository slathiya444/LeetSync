class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(row, col):
            ## base cases
            if row == m-1 and col == n-1:
                return 1
            
            if row >= m or col >= n:
                return 0

            return dp(row+1, col) + dp(row, col+1)
        return dp(0, 0)

        
