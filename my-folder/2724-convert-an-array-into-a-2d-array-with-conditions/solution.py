class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        count = defaultdict(int)
        res = []

        for i in nums:
            row = count[i]
            if row == len(res):
                res.append([])

            res[row].append(i)
            count[i] += 1

        return res  

        
