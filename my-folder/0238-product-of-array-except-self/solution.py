class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # construct left and right products
        n = len(nums)
        result = [0]*n
        result[0] = 1

        # First update the result with left products in result:
        for i in range(1, n):
            result[i] = result[i-1]*nums[i-1]

        R = 1;
        for i in reversed(range(n)):
            result[i] = result[i] * R
            R *= nums[i]

        return result
        
