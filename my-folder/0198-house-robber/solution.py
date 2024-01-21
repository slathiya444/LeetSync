class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * (len(nums))
        res[0] = nums[0]
        if len(nums) == 1:
            return res[0]
        res[1] = max(nums[0], nums[1])
        if len(nums) ==2:
            return res[1]
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2]+nums[i])

        return res[-1]
