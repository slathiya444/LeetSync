class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        res = -1

        for num in nums:
            if num < sum: res = sum + num
            sum += num

        return res
        
