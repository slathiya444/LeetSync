class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        # a, b = s[:int(n/2)], s[int(n/2):]
        ## find the vowel in a
        ## find the vowel in b

        # return vowel in a == vowel in b
        return self.countVowel(0, n//2, s) == self.countVowel(n//2, n, s)

    def countVowel(self, start: int, end: int, target: str) -> int:
        count = 0
        for char in range(start, end):
            if target[char] in "aeiouAEIOU":
                count += 1
        return count
        
