class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def get_count(string):
            return collections.Counter(string)

        return sum((get_count(t) - get_count(s)).values())
