class Solution:
    def minimumLength(self, s: str) -> int:
        f, l = 0, len(s)-1
        while f < l and s[f] == s[l]:
            ## check all firsts
            char = s[f]
            while f <= l and s[f] == char:
                f += 1

            ## check all lasts
            while f <= l and s[l] == char:
                l -= 1

        return len(s[f:l+1])
        
        
