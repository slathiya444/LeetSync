class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## find the sum of all numbers
        n = len(nums)
        sum_of_all = n*(n+1) / 2
        sum_of_nums = sum(nums)

        return int(sum_of_all - sum_of_nums)
        
