class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count, res = Counter(s), ""

        sorted_count = dict(sorted(count.items(), key = lambda x:x))
        for char in order:
            res += sorted_count.get(char, 0)*char
            if char in sorted_count:
                del sorted_count[char]

        for key, value in sorted_count.items():
            res += value*key
        return res
        
