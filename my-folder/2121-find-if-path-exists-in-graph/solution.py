class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = deque([source])

        dic = defaultdict(list)
        for fr, to in edges:
            dic[fr].append(to)
            dic[to].append(fr)

        visited = set([source])
        while q:
            node = q.popleft()

            if node == destination:
                return True

            for next_node in dic[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)

        return False

        
