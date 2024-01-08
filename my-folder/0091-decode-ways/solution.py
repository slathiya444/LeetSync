class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(index):

            ##base cases
            if index in dp:
                return dp[index]
            
            if s[index] == "0":
                return 0

            ## for single digits
            res = dfs(index+1)

            # for double digits, it is ok for all 10 to 19 values, as all of them are less then 26.
            # but when it comes to start with 2, 
            # other digit should be 0 to 6 only for making combine digit value < 26.
            if (index+1 < len(s) and (s[index] == "1" or s[index] == "2" and s[index+1] in "0123456")):
                res += dfs(index+2)
            dp[index] = res
            return res

        return dfs(0)

