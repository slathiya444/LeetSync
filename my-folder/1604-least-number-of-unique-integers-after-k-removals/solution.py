class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # count = collections.Counter(arr)
        count = Counter(arr)
        
        freq = sorted(list(count.values()))
        print(freq)
        idx = 0
        while idx <= len(freq)-1 and freq[idx] <= k :
            k -= freq[idx]
            idx += 1
            

        return len(freq) - idx
