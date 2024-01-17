class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(collections.Counter(arr).values()) == len(set(collections.Counter(arr).values()))
