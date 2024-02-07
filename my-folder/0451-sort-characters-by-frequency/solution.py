class Solution:
    def frequencySort(self, s: str) -> str:
        dd = collections.Counter(s)

        res = ''
        sorted_values = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_values.items():
            res = res + key*value

        return res
        
