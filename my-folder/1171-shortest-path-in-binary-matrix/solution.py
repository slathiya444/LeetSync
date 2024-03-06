class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # row, col, and length to reach there
        visited = set((0, 0))
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]

        ## BFS
        while q:
            r, c, l = q.popleft()
            if (min(r, c)<0 or max(r, c)>=N or grid[r][c]):
                continue

            if r == N-1 and c == N-1:
                return l

            for nr, nc in direction:
                new_row, new_col = r+nr, c+nc
                if (new_row, new_col) not in visited:
                    q.append([new_row, new_col, l+1])
                    visited.add((new_row, new_col))
        return -1
