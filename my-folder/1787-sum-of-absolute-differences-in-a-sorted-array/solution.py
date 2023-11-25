class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        left_sum = 0
        result = []

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            left_count = abs(i*nums[i] - left_sum)
            right_count = abs((n-i-1)*nums[i] - right_sum)
            left_sum += nums[i]

            result.append(left_count + right_count)




        return result  
