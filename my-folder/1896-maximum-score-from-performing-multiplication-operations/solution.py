class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache
        def dp(iteration, left_value, right_value):
            ## base cases
            if iteration == len(multipliers):
                return 0

            # right_value = len(nums)-1-(iteration - left_value)

            ### Recurance Relation
            res = max(
                multipliers[iteration]* nums[left_value] + dp(iteration+1, left_value+1, right_value), 
                multipliers[iteration]* nums[right_value] + dp(iteration+1, left_value, right_value-1)
                )

            return res

        n, m = len(nums), len(multipliers)
        return dp(0, 0, n-1)
        
