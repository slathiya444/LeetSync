class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                count += 1

            else:
                count = 1
            
            res = max(res, count)

        return res

        
