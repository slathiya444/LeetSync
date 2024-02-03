class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        cache = [None] * N
        has_cache = [False] * N

        # @lru_cache(None)
        def dp(idx):
            ## base cases
            if idx >= N:
                return 0

            if has_cache[idx]:
                return cache[idx]

            ## recurance relation
            best = 0
            curr_max = 0
            for i in range(k):
                if idx+i >= N:
                    break
                print(idx, i)
                curr_max = max(arr[idx+i], curr_max)
                best = max(best, curr_max * (i+1) + dp(idx+1+i))
                has_cache[idx] = True
                cache[idx] = best

            return best

        return dp(0)
