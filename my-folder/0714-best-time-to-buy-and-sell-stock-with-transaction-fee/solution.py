class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dp(i, hold):
            ## base cases
            nonlocal profit
            if i >= len(prices):
                return 0

            ## recurance relation
            do_nothing = dp(i+1, hold)
            if hold:
                profit = max(do_nothing, prices[i] - fee + dp(i+1, 0))

            else:
                profit = max(do_nothing, -prices[i]+dp(i+1, 1))

            return profit

        profit = 0
        return dp(0, 0)
        
