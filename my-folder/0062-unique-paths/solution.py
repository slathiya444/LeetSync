class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(row, col):
            ## base cases
            if row + col == 0:
                return 1

            ways = 0

            ## recurance relation
            if row > 0:
                ways += dp(row-1, col)

            if col > 0:
                ways += dp(row, col-1)

            return ways

        return dp(m-1, n-1)

        
