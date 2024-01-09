class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(r, c):
            ## base cases:
            if c >= n or c < 0:
                return float('inf')
            if r == m-1:
                return matrix[r][c]

            ## recurances
            return matrix[r][c] +  min(dp(r+1, c+1), dp(r+1, c), dp(r+1, c-1))


        m, n = len(matrix), len(matrix[0])
        return min([dp(0, j) for j in range(n)])
        
