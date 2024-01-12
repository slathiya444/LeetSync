class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        root = [i for i in range(n)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            parentx = find(x)
            parenty = find(y)

            if parentx == parenty:
                return False

            root[parentx] = parenty

            return True

        res = n
        for edge in edges:
            if union(edge[0], edge[1]):
                res -= 1

        return res       
