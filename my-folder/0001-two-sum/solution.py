class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maping = {}
        for idx, i in enumerate(nums):
            diff = target-i
            if diff in maping:
                return [idx, maping[diff]]
            else:
                maping[i] = idx
