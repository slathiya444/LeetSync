class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])

            else:
                res[-1][1] = max(end, res[-1][1])
        
        return res
        
