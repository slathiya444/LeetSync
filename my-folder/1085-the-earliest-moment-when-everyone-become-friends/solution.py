class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentx = find(x)
            parenty = find(y)

            if parentx == parenty:
                return False
            
            parent[parentx] = parenty
            return True

        group = n
        logs = sorted(logs, key=lambda x: x[0])
        for log in logs:
            if union(log[1], log[2]):
                group -= 1
                if group == 1:
                    return log[0]

        return -1
        return res


            
        
