class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(remaining_amount):
            ## base cases
            if remaining_amount == 0:
                return 0

            if remaining_amount < 0:
                return -1

            res = math.inf
            ## recurance relation
            for coin in coins:
                remaining = dp(remaining_amount - coin)
                if remaining != -1:
                    res =  min(res, 1+remaining)

            return res if res != math.inf else -1

        return dp(amount) 
        
