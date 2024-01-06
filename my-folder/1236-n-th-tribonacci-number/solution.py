class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(i):
            if i in [0,1]:
                return i

            if i == 2:
                return 1
            if i not in cache:
                cache[i] = res = dp(i-1) + dp(i-2) + dp(i-3)
            return cache[i]

        cache = {}
        return dp(n)
        
