class Solution:
    def minCost(self, house: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        max_cost = math.inf  # max_cost is used to represent impossible.
        N = len(house)
        @lru_cache(None)
        def dp(index, pre_color, neighbour_count):

            ## base cases
            if index == N:
                if neighbour_count == target:
                    return 0
                return max_cost

            if neighbour_count > target:
                return max_cost

            ## recurance relation
            # if the house is not painted, that mean house[index] == 0
            if house[index] == 0:
                best = max_cost
                # not colored, then we will try to color with diffen=rent color possible
                for color in range(1, n+1):
                    if color == pre_color:
                        best = min(best, cost[index][color-1] + dp(index+1, color, neighbour_count))
                    else:
                        best = min(best, cost[index][color-1] + dp(index+1, color, neighbour_count+1))

                return best

            # if the house is already painted, then we need to check if the house color is same as previous
            else:
                if house[index] == pre_color:
                    return dp(index+1, house[index], neighbour_count)
                else:
                    return dp(index+1, house[index], neighbour_count+1)

        result = dp(0, 0, 0)
        return result if result != max_cost else -1


        
