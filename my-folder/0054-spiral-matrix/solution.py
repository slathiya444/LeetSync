class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, top = 0, 0
        right, bottom = cols, rows
        res = []
        visited = set()

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for j in range(top, bottom):
                res.append(matrix[j][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break

            for k in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][k])
            bottom -= 1
            for l in range(bottom-1, top-1, -1):
                res.append(matrix[l][left])
            left += 1

        return res
