class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        words.append("")
        for i in words:
            if i[::-1] == i:
                return i
