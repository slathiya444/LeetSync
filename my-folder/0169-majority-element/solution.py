class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for item in counts:
            if counts[item] >= len(nums)/2:
                return item
        
