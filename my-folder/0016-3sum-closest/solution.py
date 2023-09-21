class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = None
        closet = float('inf')
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                addition = nums[i]+nums[left]+nums[right] 
                if addition > target:
                    right -= 1
                elif addition < target:
                    left +=1
                else:
                    return addition
                
                if abs(addition-target) < abs(closet - target):
                    closet = addition
                
        return closet
