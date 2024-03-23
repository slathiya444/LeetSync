class Solution:
    def removeVowels(self, s: str) -> str:
        remove = ['a', 'e', 'i', 'o', 'u']
        return "".join(val for val in s if val not in remove)
        
