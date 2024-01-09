class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for i in nums:
            max_profit = max(first + i, second)
            first = second
            second = max_profit
        return second
        
