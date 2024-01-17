class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(node):
            if node == destination:
                return True

            ## if the node is not seen yet
            if not seen[node]:
                seen[node] = True
                for next_node in graph[node]:
                    if dfs(next_node):
                        return True

            return False

        return dfs(source)
        
