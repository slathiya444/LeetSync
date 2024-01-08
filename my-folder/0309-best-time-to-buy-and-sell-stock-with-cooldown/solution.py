class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(current_day, hold):
            ## base cases
            # if current day is more then the length of prices, then we can not make a trade as there is no price left in array
            if current_day >= len(prices):
                return 0

            ## recursive relations

            do_nothing = dp(current_day+1, hold)
            profit = 0

            # if we hold, then sell or do nothing
            # if you sell, next call will be on i+2nd day, and after sell, hold will be 0
            if hold:
                profit = max(do_nothing, prices[current_day] + dp(current_day+2, 0))
            # if we do not hold, buy or do nothing
            # if you buy, you will pay the price and make hold to 1
            else:
                profit = max(do_nothing, -prices[current_day] + dp(current_day+1, 1))

            return profit

        return dp(0, 0)
        
