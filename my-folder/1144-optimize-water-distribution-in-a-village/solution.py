class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        root = [i for i in range(n+1)]
        rank = [0] * (n+1)
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty: ## indicate cycle
                return False

            if rank[rootx] > rank[rooty]:
                root[rooty]= rootx
            elif rank[rootx] < rank[rooty]:
                root[rootx]= rooty
            else:
                root[rooty] = rootx
                rank[rootx] += 1

            return True

        cost_map = [] ## (house1, house2, cost)
        for i in range(len(wells)):
            cost_map.append((0, i+1, wells[i])) ## reserve 0 for well index

        for h1, h2, cost in pipes:
            cost_map. append((h1, h2, cost))

        cost_map.sort(key = lambda x: x[2])
        res = 0
        for house1, house2, cost in cost_map:
            if union(house1, house2):
                res += cost

        return res

            

        
