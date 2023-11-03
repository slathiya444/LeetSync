class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # if len(nums) == 0 or len(nums) == 1:
        #     return False
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False


