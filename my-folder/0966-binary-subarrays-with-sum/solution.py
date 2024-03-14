class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(required_total):
            if required_total < 0:
                return 0

            res = 0
            left, current_sum = 0, 0

            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > required_total:
                    current_sum -= nums[left]
                    left += 1
                res += (right - left + 1)

            return res

        return helper(goal) - helper(goal-1)
