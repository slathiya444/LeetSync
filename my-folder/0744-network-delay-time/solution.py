class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        ## adjacensy list
        for src, dst, wei in times:
            edges[src].append((dst, wei))

        min_heap = [(0, k)] # heap format : (weight, source)
        visited = set()
        res = 0
        while min_heap:
            weight, source = heapq.heappop(min_heap)
            if source in visited:
                continue

            visited.add(source)
            res = max(res, weight)

            for dst2, weight2 in edges[source]:
                heapq.heappush(min_heap, [weight+weight2, dst2])

        return res if len(visited) == n else -1

        
        
