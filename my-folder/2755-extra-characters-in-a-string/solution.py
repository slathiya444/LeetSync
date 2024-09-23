class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        # memoization
        records = {}
        
        def dfs(i):
            
            ## base case
            if i == len(s):
                return 0
            
            if i in records:
                return records[i]
            
            res = 1 + dfs(i+1) # to skip the current char
            for j in range(i, len(s)):
                # fetch the substring and compare
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1))
            
            records[i] = res
            return res
        
        ## make a recursive call
        return dfs(0)
