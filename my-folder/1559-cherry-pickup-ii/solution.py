class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row_c, col_c = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(row, col1, col2):
            ## base cases
            if col1 < 0 or col2 < 0 or col1 >= col_c or col2 >= col_c:
                return -inf

            res = 0
            res += grid[row][col1]
            # if they are not in same column:
            if col1 != col2:
                res += grid[row][col2]

            ## recurance relation
            if row != row_c-1:
                res += max(dp(row+1, new_col1, new_col2)
                            for new_col1 in [col1, col1+1, col1-1]
                            for new_col2 in [col2, col2+1, col2-1]
                )

            return res

        return dp(0, 0, col_c-1)       
