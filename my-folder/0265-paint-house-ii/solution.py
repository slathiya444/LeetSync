class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        houses, colors = len(costs), len(costs[0])
        inf = 10 ** 20

        @lru_cache(None)
        def dp(house, last_color):
            ## base cases
            best = inf

            if house == houses:
                return 0

            ## recurance relation
            for color in range(colors):
                if color != last_color:
                    best = min(best, dp(house+1, color) + costs[house][color])

            return best

        return dp(0, -1)
        
