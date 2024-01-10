class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dp(i, last_v):
            total = 1
            if i>1:
                if last_v == 'a':
                    total = (dp(i-1, 'e') + dp(i-1, 'i') + dp(i-1, 'u')) % mod
                if last_v == 'e':
                    total = (dp(i-1, 'i') + dp(i-1, 'a')) % mod
                if last_v == 'i':
                    total = (dp(i-1, 'e') + dp(i-1, 'o')) % mod
                if last_v == 'o':
                    total = (dp(i-1, 'i')) % mod
                if last_v == 'u':
                    total = (dp(i-1, 'i') + dp(i-1, 'o')) % mod
            return total

        return sum(dp(n, vowel) for vowel in 'aeiou') % mod
