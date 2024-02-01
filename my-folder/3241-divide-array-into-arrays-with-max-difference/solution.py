class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans : List[List[int]] = []

        ## after sort, do 3rd element - first element, 
        # if that is less then k, that means it is valid triplet because of sort
        # in sorted triplet, diff(3rd - first) is greter then diff(second - third)

        for i in range(0, len(nums), 3): # this will loop over triplet
            if nums[i+2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])

        return ans

        
