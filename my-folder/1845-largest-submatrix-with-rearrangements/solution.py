class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ans = 0
        
        prev = c * [0]

        for row in range(r):
            for col in range(c):
                if matrix[row][col] != 0 and row>0:
                    matrix[row][col] += matrix[row - 1][col]

        for i in range(r):
            sorted_ = sorted(matrix[i], reverse = True)
            for j in range(c):
                ans = max(ans, sorted_[j] * (j+1))

            

        return ans


        
