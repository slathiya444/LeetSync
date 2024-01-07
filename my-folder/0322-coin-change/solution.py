class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(remaining_amount):
            ## base cases
            if remaining_amount < 0:
                return -1
            if remaining_amount == 0:
                return 0

            ## recurance relation
            res = float('inf')
            for j in range(len(coins)):
                remaining = dp(remaining_amount - coins[j])
                if remaining != -1:
                    res = min(res, remaining+1)

            return res if res != float('inf') else -1

        return dp(amount)
        
