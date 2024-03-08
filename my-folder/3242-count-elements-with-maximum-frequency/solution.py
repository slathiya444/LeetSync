class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mapp = {}
        for i in nums:
            mapp[i] = mapp.get(i, 0) + 1

        value_mapp = {}
        maxi = max(mapp.values())
        for i in mapp.values():
            value_mapp[i] = value_mapp.get(i, 0) + 1

        return maxi*value_mapp[maxi]


        
