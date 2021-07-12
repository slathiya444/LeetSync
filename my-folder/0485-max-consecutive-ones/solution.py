class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # ones = []
        # size = 0
        # for num in nums:
        #     if  num == 1:
        #         ones.append(num)
        #     elif (num == 0 and size < len(ones)) or :
        #         size = len(ones)
        #         ones = []
        # return size
        counter = 0
        longest = 0
        for num in nums:
            if num == 1:
                counter += 1
            else :
                longest = max(longest,counter)
                counter = 0

        return max(counter,longest)
            
        
