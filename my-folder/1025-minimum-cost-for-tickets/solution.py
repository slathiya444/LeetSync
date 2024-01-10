class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        valid_days = {
            costs[0] : 1,
            costs[1] : 7,
            costs[2] : 30
        }
        @lru_cache(None)
        def dp(day, remaining_days):
            ## base cases
            # if we have travelled all the days required, then there is n o further cost
            if day == n:
                return 0
            
            ## recurance relation
            # if we already have a valid bus pass, we do not need to buy on a travel day
            if remaining_days >= days[day]:
                return dp(day+1, remaining_days)

            # if we do not have valid bus pass on travel day, we need to buy one.
            # for the best options, we need to find min from buying all three options
            else:
                return min([cost + dp(day+1, days[day] + d_count- 1) for cost, d_count in valid_days.items()])
                
        return dp(0, 0)
        
