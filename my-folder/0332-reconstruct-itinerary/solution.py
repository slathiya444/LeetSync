class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(node):
            if node in graph:
                while graph[node]:
                    neighbor = graph[node].pop()
                    dfs(neighbor)
            result.append(node)

        graph = {sc: [] for sc, dt in tickets}
        for src, dst in tickets:
            graph[src].append(dst)

        for key in graph:
            graph[key].sort(reverse=True)

        result = []
        dfs("JFK")
        return result[::-1]
            
