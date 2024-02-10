class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dp(index):
            ## base cases
            if index < 0:
                return True

            if index in cache:
                return cache[index]

            ## recurance relation
            for word in wordDict:
                if s[index - len(word) + 1 : index+1] == word and dp(index - len(word)):
                    cache[index] = True
                    return True
            cache[index] = False
            return False

        return dp(len(s)-1)

        
