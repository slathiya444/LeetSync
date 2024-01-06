class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        repeat = collections.Counter(nums)
        
        @cache
        def dp(index):
            ## base cases
            if index == 0:
                return 0

            if index == 1:
                return repeat[1]

            ## recursive relation
            return max(dp(index-2) + (repeat[index] * index), dp(index-1))
            
        return dp(max(nums))
