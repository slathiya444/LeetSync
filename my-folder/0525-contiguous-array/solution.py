class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0

        diff_mapp = {} #count[0] - count[1] -> idx
        for idx, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1

            if zero - one not in diff_mapp:
                diff_mapp[zero - one] = idx
            
            if zero == one:
                res = zero + one
            else:
                i = diff_mapp[zero - one]
                res = max(res, idx - i)

        return res

             
                
