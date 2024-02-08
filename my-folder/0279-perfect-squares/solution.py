class Solution:
    
    def numSquares(self, n: int) -> int:
        res = float('inf')
        def dp(n):
            nonlocal res
            nonlocal cache
            ## base case
            if n == 0: return 0
            if n in cache:
                return cache[n]

            ## recurance relation
            for i in range(1, math.floor(math.sqrt(n))+1):
                res = min(res, 1 + dp(n - (i*i)))
            
            cache[n] = res
            return res
        
        cache = {}
        return dp(n)

