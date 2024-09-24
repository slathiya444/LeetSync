class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_hash = set()

        # making sure arr1 is smaller, if not, make it.
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        # now add bigger array's prefixes to hashset
        for item in arr2:
            while item not in prefix_hash:
                prefix_hash.add(item)
                item = item // 10

        res = 0
        for item2 in arr1:
            while item2 and item2 not in prefix_hash:
                item2 = item2 // 10
            
            if item2:
                res = max(res, len(str(item2)))
        return res

        
