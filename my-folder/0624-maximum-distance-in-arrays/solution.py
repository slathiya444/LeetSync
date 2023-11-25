class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        minimum, maximum = 100000, -100000
        for i in arrays:
            result = max(max(i[-1]-minimum, maximum-i[0]), result)
            minimum, maximum = min(minimum, i[0]), max(maximum, i[-1])
        
        return result

        
