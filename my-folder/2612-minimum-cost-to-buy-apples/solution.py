class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        ### Dikstra
        adj = defaultdict(list)
        for u, v, c in roads:
            adj[u-1].append((v-1, c))
            adj[v-1].append((u-1, c))

        heap = [(c, i) for i, c in enumerate(appleCost)]
        heapify(heap)
        minCost = appleCost.copy()
        found = 0
        while heap:
            cost, node = heappop(heap)
            if cost > minCost[node]:
                continue
            for neigh, dist in adj[node]:
                neigh_cost = dist * (k + 1) + cost
                if neigh_cost < minCost[neigh]:
                    minCost[neigh] = neigh_cost
                    heappush(heap, (neigh_cost, neigh))
        return minCost
