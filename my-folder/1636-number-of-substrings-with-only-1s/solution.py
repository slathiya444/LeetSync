class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        counter = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                continue

            elif i==0 or s[i] == s[i-1]:
                counter += 1
            
            else:
                counter = 1

            ans = (ans + counter) % mod

        return ans
        
