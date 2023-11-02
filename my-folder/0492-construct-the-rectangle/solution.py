class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(math.sqrt(area)) #14
        while(True):
            w = area/l
            if w.is_integer():
                if l>w:
                    return [l, int(w)]
                else:
                    return [int(w), l]
            else:
                l-=1
        
