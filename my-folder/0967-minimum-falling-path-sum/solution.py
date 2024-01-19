class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(r, c):

            ## base cases
            if c >= n or c < 0:
                return inf

            if r == m-1:
                return matrix[r][c]

            ## recursive iteration
            return matrix[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1))

        inf = 10 ** 10
        m, n = len(matrix), len(matrix[0])
        return min([dp(0, j) for j in range(n)])
        
