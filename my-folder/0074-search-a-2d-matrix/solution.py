class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])

        left, right = 0, row*col - 1
        while left <= right:
            pivot_index = (left + right) // 2
            pivot_element = matrix[pivot_index // col][pivot_index % col]
            if target == pivot_element:
                return True
            
            else:
                if target <  pivot_element:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1
            
        return False
        
