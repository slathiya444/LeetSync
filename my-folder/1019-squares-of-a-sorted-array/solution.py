class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ## as the input is sorted, zero should be in middle because of negetive values,
        ## but square values are the same (eg. (-6) and 6 have the same value 36)
        ## so we can start from highest square values
        res = [] # return will be reverse of this
        left, right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1

        return res[::-1]

        
