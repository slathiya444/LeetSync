class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # iterate over each column, and check forn a match
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):

                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row+1][col+1]

                else:
                    dp_grid[row][col] = max(
                        dp_grid[row+1][col],
                        dp_grid[row][col+1]
                    )

        return dp_grid[0][0]
        
