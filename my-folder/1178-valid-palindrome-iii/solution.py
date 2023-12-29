class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        n = len(s)
        has_cached = [[False] * (n+1) for _ in range(n+1)]
        cache = [[None] * (n+1) for _ in range(n+1)]

        def validStr(left, right):
            
            best = 1001
            if left >= right:
                return 0

            if has_cached[left][right]:
                return cache[left][right]

            ## keep forst and last element for palindrom
            if s[left] == s[right]:
                best = min(best, validStr(left+1, right-1))

            ## remove element if doesnot match in palindrom process
            best = min(best, validStr(left+1, right)+1)
            best = min(best, validStr(left, right-1)+1)

            has_cached[left][right] = True
            cache[left][right] = best

            return best

        return validStr(0, n-1) <= k
