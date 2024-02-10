class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = 1
        cur_max = 1

        for n in nums:
            tmp = cur_min * n
            cur_min = min(n, cur_max * n, cur_min * n)
            cur_max = max(n, cur_max * n, tmp)

            res = max(res, cur_max)

        return res




        
