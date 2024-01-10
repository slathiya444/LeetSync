class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            # If we are at the end of strings, that means we have computed everything
            if i == len(s1) and j == len(s2):
                return True

            # now check for the character in s1:
            if i < len(s1) and s1[i] == s3[i+j] and dp(i+1, j):
                return True

            # if character from s1 is not matching, then will check character from s2
            if j < len(s2) and s2[j] == s3[i+j] and dp(i, j+1):
                return True

            return False

        if len(s1) + len(s2) != len(s3):
            return False
        return dp(0, 0)
