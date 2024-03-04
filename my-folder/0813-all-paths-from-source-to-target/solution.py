class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        dest = len(graph)-1

        res = []
        q = deque([[0]])

        while q:
            node = q.popleft()

            if node[-1] == dest:
                res.append(node)

            for next_node in graph[node[-1]]:
                q.append(node + [next_node])

        return res

            

        
