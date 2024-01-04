class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for c in count.values():
            if c == 1:
                return -1
            
            required_op = math.ceil(c/3)
            res += required_op
        return res
        
