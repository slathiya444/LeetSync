class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = -1, -1

        for i in range(1, len( nums)+1):
            count = nums.count(i)
            if count == 2:
                duplicate = i

            elif count == 0:
                missing = i

        return [duplicate, missing]
        
