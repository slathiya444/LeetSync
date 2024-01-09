class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        m = len(costs)
        n = len(costs[0])
        dp = [[0] * n for _ in range(m)]
        
        ## base case
        dp[0] = costs[0]

        for house in range(1, m):
            current_cost = costs[house]
            # paint the current house in red(0th) color
            # for that previous house could be blue(1st) or green(2nd) only.
            dp[house][0] = current_cost[0] + min(dp[house-1][1], dp[house-1][2])

            # paint the current house in blue(1st) color
            # for that previous house could be red(oth) or green(2nd) only.
            dp[house][1] = current_cost[1] + min(dp[house-1][0], dp[house-1][2])

            # paint the current house in green(2nd) color
            # for that previous house could be red(0th) or blue(1st) only.
            dp[house][2] = current_cost[2] + min(dp[house-1][0], dp[house-1][1])

        return min(dp[-1])
        
