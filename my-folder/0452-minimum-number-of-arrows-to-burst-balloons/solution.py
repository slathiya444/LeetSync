class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points = sorted(points, key = lambda x : x[0])
        new_point = points[0]
        
        for idx in range(1, len(points)):
            # overlaping
            if new_point[1] >= points[idx][0]:
                # res += 1
                new_point = [max(new_point[0], points[idx][0]), min(new_point[1], points[idx][1])]
            
            else:
                res += 1
                new_point = points[idx]
                
        res += 1
        
        return res
        
