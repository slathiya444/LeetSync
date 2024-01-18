class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) -1
        ans = []

        def dfs(node, path):
            if node == end:
                ans.append(path[:])
                return

            for nxt in graph[node]:
                dfs(nxt, path+[nxt])

        dfs(0, [0])
        return ans

            

        
