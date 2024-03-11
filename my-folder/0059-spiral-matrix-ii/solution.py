class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # rows, cols = n, n
        left, top = 0, 0
        right, bottom = n, n
        res = [[1] * n for _ in range(n)]
        prev = 1

        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = prev
                prev += 1
            top += 1

            for j in range(top, bottom):
                res[j][right-1] = prev
                prev +=1
            right -= 1

            for k in range(right-1, left-1, -1):
                res[bottom-1][k] = prev
                prev += 1
            bottom -= 1
            
            for l in range(bottom-1, top-1, -1):
                res[l][left] = prev
                prev += 1
            left += 1

        return res
        
