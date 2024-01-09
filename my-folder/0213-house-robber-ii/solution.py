class Solution:
    def rob(self, nums: List[int]) -> int:
        skip_first = self.helper(nums[1:])
        skip_last = self.helper(nums[:-1])
        return max(nums[0], skip_first, skip_last)

    def helper(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in nums:
            max_profit = max(first + i, second)
            first = second
            second = max_profit
        return second
        
