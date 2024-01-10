class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = (10 ** 9) + 7
        @lru_cache(5000)
        def dp(dice, remaining_target):
            ## base cases
            if remaining_target <= 0:
                return 0

            if dice == 1:
                if remaining_target <= k:
                    return 1
                else: return 0

            ## recurance relation
            return sum([dp(dice-1, remaining_target-i) for i in range(1, k+1)])

        return dp(n, target) % mod
