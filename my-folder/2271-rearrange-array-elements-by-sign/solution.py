class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j = 0, 1
        for num in nums:
            if num > 0:
                res[i] = num
                i += 2
            else:
                res[j] = num
                j += 2
        return res


