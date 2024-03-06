class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N= len(points)

        ## create adjucensy list
        adj = {i:[] for i in range(N)} # value for key i should be like: [cost, dest]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        ## prim's
        res = 0
        visited = set()
        min_heap = [[0, 0]]  # [cost, nth node]
        while len(visited) < N: # because we need exactly (N-1) edges with weights
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)

            for nei_cost, nei in adj[node]: #neighbour : [cost, nth node]
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])

        return res


        
