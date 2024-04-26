class DisjointSet:
    def __init__(self, n):
        # Initialize each node to be its own parent (self loop) and size of each set to 1.
        self.size = [1] * n
        self.parent = [i for i in range(n)]

    def findParent(self, u):
        # Path compression: find the representative member of the set containing 'u'.
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findParent(self.parent[u])  # Recursively find and update parent.
        return self.parent[u]

    def unionBySize(self, u, v):
        # Union by size: join two sets by connecting the smaller set to the larger one.
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return False  # 'u' and 'v' are already in the same set.
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]  # Initialize the grid.

        disjointSet = DisjointSet(n * m)  # Create DisjointSet for every cell.
        islands_count = []  # Stores count of islands after each addition.
        count = 0  # Count of islands.
        for position in positions:
            r, c = position
            if grid[r][c] == 0:
                count += 1  # Increment island count for each new land.
            grid[r][c] = 1
            # Check all 4 adjacent directions and perform union operations.
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c]:
                    if disjointSet.unionBySize(r * n + c, new_r * n + new_c):
                        count -= 1  # Decrement island count if two lands are connected.
            islands_count.append(count)
        return islands_count
        
