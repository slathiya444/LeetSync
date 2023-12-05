class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            cur_target = numbers[i] + numbers[j]
            if cur_target > target:
                j -= 1
            elif cur_target < target:
                i += 1
            elif cur_target == target:
                return [i+1, j+1]

        return false

            
        
