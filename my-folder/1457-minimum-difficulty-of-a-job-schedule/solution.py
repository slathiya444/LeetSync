class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(index, remainDays):

            if remainDays == 0:
                if index == n:
                    return 0
                else:
                    return sys.maxsize

            if index == n:
                if remainDays == 0:
                    return 0
                else:
                    return sys.maxsize

            ans = sys.maxsize
            curr_max = 0
            for i in range(index, n):
                curr_max = max(curr_max, jobDifficulty[i])
                ans = min(ans, curr_max + dp(i+1, remainDays-1))

            return ans

        n = len(jobDifficulty)
        if d>n:
            return -1

        return dp(0, d)
        
