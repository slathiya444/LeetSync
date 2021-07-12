class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(OrderedDict.fromkeys(nums)) 
        return len(nums)
                
                
