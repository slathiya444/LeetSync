class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        root = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            ## if both has the same root, and we make union of them, there will be a cycle.
            ## and if cycle, not a valid tree
            if rootx == rooty:
                return False
            
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                root[rootx] = rooty
            else:
                rank[rootx] += 1
                root[rooty] = rootx

            ## if we can establish the union. that means that is a valid tree until this union, 
            ## and process next edge
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False

        return True



        
