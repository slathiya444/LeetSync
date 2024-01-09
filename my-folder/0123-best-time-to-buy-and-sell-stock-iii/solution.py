class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(current_day, hold, remaining_transaction):
            ## base cases
            if remaining_transaction == 0:
                return 0

            if current_day == len(prices):
                return 0

            ## recusrance relation
            # if we hold already, then sell or do nothing

            do_nothing = dp(current_day+1, hold, remaining_transaction)

            if hold:
                profit = max(do_nothing, prices[current_day] + dp(current_day+1, 0, remaining_transaction-1))
            # if we do not holf, then buy or do nothing
            else:
                profit = max(do_nothing, -prices[current_day] + dp(current_day+1, 1, remaining_transaction))

            return profit

            # if we do not hold, then buy or do nothing

        profit = 0
        k = 2
        return dp(0, 0, k)
