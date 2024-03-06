class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ## find the rotten orange and fresh oranges to start BFS
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        ## Now we have to make sure every fresh orange will be rotten, even single left, return -1
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                ## new adjacent oranges
                for dr, dc in direction:
                    row, col = r+dr, c+dc
                    if (min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]) or 
                        grid[row][col] in [0, 2]):
                         continue

                    # make orange rotten
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1
        return time if fresh == 0 else -1

                
