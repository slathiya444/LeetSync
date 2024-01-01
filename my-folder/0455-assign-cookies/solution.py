class Solution:
    def findContentChildren(self, child: List[int], coockie: List[int]) -> int:
        child.sort()
        coockie.sort()

        child_served = 0
        coockie_index = 0

        while coockie_index < len(coockie) and child_served < len(child):
            if coockie[coockie_index] >= child[child_served]:
                child_served += 1
            
            coockie_index += 1
        
        return child_served
        
